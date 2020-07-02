#---CARREGANDO LIBRARY E API AZURE
library(mscstexta4r)
Sys.setenv(MSCS_TEXTANALYTICS_URL="https://brazilsouth.api.cognitive.microsoft.com/text/analytics/v2.0/", MSCS_TEXTANALYTICS_KEY= "0c5062f70b744165b55933cace3ea9b9")
textaInit()

#---CORPUS PARA ANALISE
filePath <- "D:/Data Science/Bolsonaro 2019/5mais/Grr/comentariosinfluentes.csv"
texto <- read.csv(filePath, sep=',')

request_body <- data.frame(
  language = "pt",
  id = texto$id,
  text = texto$message)

request_body <- data.frame(lapply(request_body, as.character), stringsAsFactors=FALSE)

#---ANALISE
resultado <- textaSentiment(
  documents = request_body$text,  
  languages = request_body$language
)

request_body$resultado <- resultado$results$score

write.csv(request_body,"D:/Data Science/Bolsonaro 2019/5mais/Grr/analisesentimentos.csv", row.names = FALSE)

boxplot(request_body$resultado)
plot(request_body$resultado)
