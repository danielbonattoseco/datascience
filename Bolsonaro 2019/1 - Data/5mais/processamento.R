

library(tm)
library(readtext)
library(utils)
library(stm)
library(textstem)
library(koRpus.lang.pt)

filePath <- "D:/Data Science/Facepager/Bolsonaro 2019/Data/bolsonaro2019pronto.csv"
texto <- read.csv(filePath, encoding="Latin-1")
head(texto)

# load the data as a corpus

corpus = VCorpus(VectorSource(texto),readerControl = list(reader=readPlain,language = "por"))
inspect(corpus) 

corpus = tm_map(corpus, removeWords, stopwords("portuguese"))
corpus = tm_map(corpus , stripWhitespace)

freq <- TermDocumentMatrix(corpus)

lemma_dictionary <- make_lemma_dictionary(lemma_dic, engine = 'hunspell', lang='pt')
textolematizado = lemmatize_strings(texto, dictionary = lemma_dic2) 

#lematizacao

corpusteste = TermDocumentMatrix(corpus)
corpusmatriz <- as.matrix(freq)
palavras<-row.names(corpusmatriz)

lemma_dic <- read.delim(file = "https://raw.githubusercontent.com/michmech/lemmatization-lists/master/lemmatization-pt.txt", 
                        header = FALSE, stringsAsFactors = FALSE, encoding='UTF-8')
lemma_dic <- read.delim(file = "D:/Data Science/Facepager/Bolsonaro 2019/Data/dicionarioinvertido.txt", 
                        header = FALSE, stringsAsFactors = FALSE, encoding='Latin-1', sep=' ')

names(lemma_dic2) <- c("term", "stem")

#plot

library(wordcloud)
pal = brewer.pal(9, "Blues")
pal = pal[-(1:3)]
wordcloud(corpus,max.words=100,random.order=F,colors=pal,use.r.layout=T)

freq <- TermDocumentMatrix(corpus)
freq2 <- removeSparseTerms(freq, sparse = 0.99)
matriz <- as.matrix(freq2)
matriz <- sort(rowSums(matriz),decreasing=TRUE)
matriz = data.frame(Palavra=names(matriz), Frequência=matriz)

write.csv(matriz,paste('D:/Data Science/Facepager/Bolsonaro 2019/5mais/Curtir/matrizCSV.csv', sep = ''), row.names=FALSE, quote=FALSE)
write.table(matriz, "D:/Data Science/Facepager/Bolsonaro 2019/5mais/Curtir/matrizTABLE.txt", sep="\t", row.names=FALSE, quote=FALSE)

proc <- stm::textProcessor(matriz, removenumbers = FALSE, language = "portuguese")
out <- stm::prepDocuments(proc$documents, proc$vocab, proc$meta,
                          lower.thresh = 2)
storage <- stm::searchK(out$documents, out$vocab, K = c(3:15),
                        data = out$meta)
fit <- stm(documents = out$documents, vocab = out$vocab, data = out$meta,  K = 10, max.em.its = 75, init.type = "Spectral", verbose = FALSE)