library(tm)
library(stm)
library(RColorBrewer)
library(wordcloud2)
library(wordcloud)


#----LEITURA TEXTO
filePath <- "D:/Data Science/Bolsonaro 2019/5mais/Triste/dadosnormalizados.csv"
texto <- read.csv(filePath, encoding="ASCII", sep=';')

#----TRANSFORMAR EM CORPUS
corpus = VCorpus(VectorSource(texto$message),readerControl = list(reader=readPlain,language = "por"))
corpus = tm_map(corpus, removeWords, stopwords("portuguese"))
corpus = tm_map(corpus , stripWhitespace)

#----MATRIZ DE FREQUENCIA
freq <- TermDocumentMatrix(corpus)
freq <- removeSparseTerms(freq, sparse = 0.99)
matriz <- as.matrix(freq)
matriz <- sort(rowSums(matriz),decreasing=TRUE)
matriz = data.frame(Palavra=names(matriz), Frequência=matriz)

#---AJUSTES MATRIZ
matrizajustada <- subset(matriz, Palavra != 'bolsonaro')
matrizajustada <- subset(matrizajustada, Palavra != 'presidente')
matrizajustada <- subset(matrizajustada, Palavra != 'nao')
matrizajustada <- subset(matrizajustada, Palavra != 'vai')
matrizajustada <- subset(matrizajustada, Palavra != 'pra')



#-----WORDCLOUD
library(wordcloud2)
pal = brewer.pal(9, "PuBu")
pal = pal[-(1:2)]
wordcloud2(matrizajustada, shape='circle', color = pal) 

#-----LEMATIZACAO
lemma_dic <- read.delim(file = "D:/Data Science/Facepager/Bolsonaro 2019/Data/dicionarioinvertido.txt", 
                        header = FALSE, stringsAsFactors = FALSE, encoding='Latin-1', sep=' ')
texto$message = lemmatize_strings(texto$message, dictionary = lemma_dic) 

#-----STRUCTURAL MODEL PROJECT
proc <- stm::textProcessor(texto$message, removenumbers = FALSE, language = "portuguese")
plotRemoved(proc$documents, lower.thresh = seq(1, 200, by = 100))
out <- stm::prepDocuments(proc$documents, proc$vocab, proc$meta, lower.thresh = 20)
storage <- stm::searchK(out$documents, out$vocab, K = c(3:15),
                        data = out$meta, max.em.its = 20)
plot(storage)
fit <- stm(documents = out$documents, vocab = out$vocab, data = out$meta,  K = 10, init.type = "Spectral", verbose = FALSE)

plot(fit, "summary")
plot(fit, "perspective", topics = c(9, 6))
stm::labelTopics(fit)
head(fit$theta)

