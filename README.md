# Effekt der JPEG-Bildkompression bewertet mit Maximum Likelihood Difference Scaling (MLDS) 
## Guillermo Aguilar
### Seminar: Visuelle Wahrnehmung beim Menschen und Bildqualität - WiSe 2020/21
*Dies ist nur eine **minimale** Beispieldokumentation, sie soll Ihnen eine Vorstellung davon geben, wie Sie Ihren Bericht strukturieren können. Wenn Sie mehr Bedingungen oder Bildmanipulationen, mehr Stimuli und mehr Ergebnisse zu zeigen haben, sollten Sie sie natürlich entsprechend erweitern. Behalten Sie aber die gleiche Gesamtstruktur bei.*


## 1. Fragestellung und Hypothese

Algorithmen zur Bildkomprimierung können sich spürbar auf die Bildqualität auswirken, besonders wenn wir eine hohe Komprimierung anwenden. Unsere Forschungsfrage war, wie viel Kompression wir auf ein Bild anwenden können, ohne dass die Qualitätsverschlechterung für einen menschlichen Betrachter spürbar wird. Unsere Hypothese lautet: Wenn die Bildkomprimierung die Bildqualität allmählich beeinflusst, bis sie spürbar wird, gibt es eine maximale Komprimierungsmenge, die angewendet werden kann, ohne dass der Beobachter eine Verschlechterung bemerkt. Um unsere Forschungsfrage zu beantworten, haben wir die Wahrnehmungsskalen mittels Maximum Likelihood Difference Scaling (MLDS) für verschiedene Grade der JPEG-Kompression gemessen. Unser Ansatz ähnelte der Arbeit von Charrier et al. (2007). 

## 2. Experimentelles Design

Wir haben ein Bild genommen (*Einsteins* Porträt) und 7 Stufen der JPG-Kompression angewendet. Konkret haben wir das Einstein-Bild mit sieben verschiedenen *Qualitäts*-Parameterwerten (0, 5, 10, 20, 40, 60, 80) unter Verwendung der *PIL*-Bibliothek für Python gespeichert (der Qualitätsparameter reicht von 0 bis 100). Wir haben auch das ursprüngliche, unveränderte *Einstein*-Bild (Qualität gleich 100) beigefügt. 

Zur besseren Veranschaulichung der Bildmanipulation haben wir die JPEG-Qualitätswerte in *Verzerrungswerte* umgerechnet, definiert als *Verzerrung = (100 - Qualität)*. Die folgende Abbildung zeigt den kompletten Satz der im Experiment verwendeten Stimuli.


![png](output_4_0.png)


Wir habe Wahrnehmungsskalen mittels MLDS mit der Methode der Triaden gemessen. Insgesamt gab es ${8 \choose 3}= 56$ mögliche Triadenkombinationen, die wir $n=5$ mal wiederholten, was insgesamt 280 Versuche pro Beobachter ergab.

## 3. Ergebnisse

Die folgende Abbildung zeigt die Wahrnehmungsskala, gemessen an zwei Beobachtern (dem Autor und einem naiven Teilnehmer). Wir haben das Maximum der Skala in Anlehnung an Charrier et al. (2007) auf eins normiert. 


![png](output_7_0.png)


## 4. Interpretation, mögliche Probleme, offene Fragen

Wir stellen fest, dass die Wahrnehmungsskalen für beide Beobachter flach (oder leicht negativ) sind bis zu einem Verzerrungsgrad von 60 - 80 (Qualität von 20 - 40). Die Flachheit der Skala in diesem Bereich deutet darauf hin, dass die wahrgenommene Verschlechterung der Bildqualität nicht spürbar ist. Bei Degradationswerten höher als 60 - 80 (Qualität niedriger als 20 - 40) steigen die Wahrnehmungsskalen monoton an, was darauf hinweist, dass die Bildqualität abnimmt und dies von den Beobachtern auch tatsächlich wahrgenommen wird. Diese Ergebnisse stimmen mit unserem informellen subjektiven Eindruck von Qualitätsverschlechterung überein, wenn man die erste Abbildung oben betrachtet.


Eine klare Einschränkung in unserer Arbeit ist die Tatsache, dass wir eine begrenzte Anzahl von Stimuli verwendet haben. Wir haben nur ein Bild verwendet, ein Porträtbild von *A. Einstein*, und wir haben die Wahrnehmungsskalen für nur zwei Beobachter gemessen. Eine offene Frage ist, wie sich diese Ergebnisse auf andere Arten von Bildern (z. B. Landschaften, Kunstwerke) verallgemeinern lassen und ob es mehr Variabilität zwischen den Beobachtern gibt, die mit einer kleinen Anzahl von Teilnehmern nicht erfasst werden kann.

### Referenzen
Charrier et al. (2007). Maximum likelihood difference scaling of image quality in compression-degraded images. JOSA 24 (11): 3418-26

