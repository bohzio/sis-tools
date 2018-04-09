# Sis-tools
Questo repository contiene degli scripts che ho utilizzato per l'elaborato SIS per ottimizzare e velocizzare il workflow.
Tutto è stato testato e utilizzato solamente su ubuntu 16.04

Questi sono gli scripts:
* **generate-stg** - Partendo dal file blif contenente la FSM genera in automatico un'immagine con il grafo degli stati.
* **minimize-fsm** - Minimizza in automatico il file blif contenente la FSM per poter testare velocemente le modifiche.
    * Lo script esegue state_minimize, state_assign jedi e stg_to_network e salva in un nuovo file.
* **run-test-sis** - Esegue in automatico i test strutturando quelli falliti in tabella per poter visualizzare meglio gli errori.

### Installazione

Sis-tools utilizza python 2.7. Gli scripts sono stati "testati"(:wink:) solo su ubuntu, dovrebbero funzionare anche su osx però chissà, non avendo un Mac non posso testare. 

Queste sono le dipendenze che servono.

```sh
sudo apt-get install expect
sudo apt-get install python-pip
sudo apt-get install graphviz
sudo apt-get install git
pip install graphviz
```

Una volta che tutte sono state installate potete usare questo link per clonare e aggiungere al path gli scripts.
```sh
git clone https://github.com/mattia98tr/sis-tools.git ~/.sis-tools && echo 'PATH=~/.sis-tools/:"$PATH"' >> ~/.bashrc && sudo chmod +x -R ~/.sis-tools/
```

Ora potete spostarvi nella vostra cartella del progetto e usare gli scripts.

### generate-stg
Prima di tutto dovete modificare il file blif della FSM aggiungendo alla fine e all'inizio delle transizioni i marcatori #STG-START e #STG-STOP.
Potete lasciare tutto il resto, basta soltanto che le transizioni siano comprese tra questi 2 marcatori
```
#STG-START
0------ A A 000
1--0--- A B 111
1--1--- A C 111
#STG-STOP
```
A questo punto potete lanciare il comando

```sh
generate-stg <fileFSM.blif>
```
Se tutto è andato a buon fine dovreste vedere nella cartella un file che contiene l'immagine. Il risultato sarà tipo quello seguente e ovviamente varierà a seconda del numero di nodi e dei collegamenti tra essi. (il risultato sembra migliore della generazione automatica di BVE :wink: )

![alt text](https://img.ziggi.org/k0BJhNeN.jpg)

### minimize-fsm

```sh
minimize-fsm <fileFSM.blif> <newfileFSM_min.blif>
```
Ora dovreste trovarvi con questo nuovo file <newfileFSM_min.blif> che contiene la fsm minimizzata. 

### run-test-sis

```sh
run-test-sis <test_in.txt> <test_out.txt>
```
Il file test_in deve essere come da esempio. I simulate possono cambiare l'importante è che la prima e l'ultima riga siano queste. Le parentisi < > non vanno messe ma stanno solo ad indicare che lì dentro dovete mettere i vostri nomi dei file
```
read_blif <FSMD.blif>
simulate 0 1 1 0 1 0 0 1 1 0 0 0 1
simulate 0 0 1 0 1 0 0 1 1 0 1 0 1
simulate 1 0 0 0 1 0 0 1 1 0 1 1 1
simulate 0 0 1 1 0 1 1 0 1 1 0 0 0
quit
```

Il file test_out deve essere come da esempio
```
0	0	0	0	0
0	0	0	0	0
1	1	1	1	1
1	1	1	1	1
```
Sono consapevole che con il tab il file di out non sia il massimo ma questo è il formato che ci è stato fornito dal prof.
Alla fine basta aggiungere la prima e l'ultima istruzione nel file di input poi per il resto potete copiare i file del prof.

Il risultato sarà questo:

![alt text](https://img.ziggi.org/cd0ZTdwj.jpg)



### Todos

 - Fare dei test (almeno finti:smiley:)
 - Testare su osx e creare l'url di installazione per quella piattaforma
 - Aggiungere altri scripts, magari voi avete altre idee

Se trovate errori fate pure una pull request o scrivetemi mattia.corradi.tr@gmail.com oppure contattatemi su telegram @mattia98tr


**Free Software, Hell Yeah!**

