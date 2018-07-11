
## Image Recognition Using OpenCV



# References

## References for LBPHFaceRecognizer
1. [THE CODACUS][thecodacusmain] ; Face Recognition Using OpenCV
2. [THE CODACUS][thecodacustrain] ; Face Recognition OpenCV – **Training A Face Recognizer**
3. [THE CODACUS][thecodacus] ; Face Recognition Using OpenCV - **Loading Recognizer**

### Videos
1. [Universo Discreto][UniversoDiscreto11_1] ; Como Funciona um Detector de Faces? - OpenCVLOG 11.1
2. [Universo Discreto][UniversoDiscreto11_2] ; Treinando Bases para Reconhecimento de Face  - OpenCVLOG 11.2
3. [Universo Discreto][UniversoDiscreto11_3] ; Como Funciona o Reconhecimento de Faces? - OpenCVLOG 11.3

[thecodacus]: https://thecodacus.com/face-recognition-loading-recognizer/ "thecodacus"

[thecodacusmain]: https://thecodacus.com/category/opencv/face-recognition/

[thecodacustrain]:https://thecodacus.com/face-recognition-opencv-train-recognizer/

[UniversoDiscreto11_1]: https://www.youtube.com/watch?v=gBNovV5k-9E&t=1s
[UniversoDiscreto11_2]: https://www.youtube.com/watch?v=h5z8jrW9CtY&t=1s
[UniversoDiscreto11_3]: https://www.youtube.com/watch?v=k96Tcgngk_0











# Referências

## I - Dissertações

1. [**Dissertação**, 1997] - [Deteccção de movimento e sua aplicacação á monitorização de tráfego][Dissertacao_1]  
**[06/07 - Broch] _- É interresante pra poder começar a escrever a introdução do TCC._**

[Dissertacao_1]:https://repositorio-aberto.up.pt/bitstream/10216/11449/2/Texto%20integral.pdf

---

2. [**Dissertação**, 2003] - [Um Equipamento Eletrônico de Monitoramento de Velocidade](https://www.lume.ufrgs.br/bitstream/handle/10183/6139/000437283.pdf?seq)  
**[06/07 - Broch] _- Apresenta os meios de medição de velocidade e propõe um radar utilizando processamento de imagem._**

	>"Uma câmera fica permanentemente filmando a via pública. Esta câmera deve ser capaz de gerar imagens entrelaçadas, pois o princípio para o cálculo é justamente a difereça de varredura entre as linhas ímpares e pares."

---
3. [**Dissertação**, 2015] - [Medição de posição, velocidade e aceleração utilizando
visão computacional em robôs móveis.](http://repositorio.uema.br/bitstream/123456789/160/1/EDUARDO%20HENRIQUE%20CASTRO%20MENDES.pdf)

	>"Este trabalho objetiva o desenvolvimento de um sistema para localização e medições de um robô móvel baseada em técnicas de visão computacional utilizando a **biblioteca OpenCV**. O sistema captura imagens de um robô móvel em um plano a partir de uma câmera montada no teto do ambiente."

---
## II - Teses

1. [**Tese**, 2003] - [Metodologia para detecção rápida de movimento em sequência de imagens](http://www.teses.usp.br/teses/disponiveis/76/76132/tde-05052008-173600/publico/IsauraOliveira_D.pdf)  
**[09/07 - Broch] _- Ver sobre o Diagrama de Agulhas_**

---
## III - Artigos

1. [**Artigo**, 2014] - [Proposal a Vehicle Speed Measuring System Using Image Processing](https://ieeexplore.ieee.org/document/6845938/?reload=true)

---
2. [**Artigo**, 2011] - [Speed Detection Camera System using Image Processing
Techniques on Video Streams ](http://www.ijcee.org/papers/418-E1077.pdf)

---
3. [**Artigo**, 2015] - [Vehicle Speed Measurement and Number Plate Detection using
Real Time Embedded System](https://drive.google.com/drive/folders/13h7VvLGrVAD64xZz1ZDHy_5ILGW7xsdF)  
**[09/07 - Broch] _- Tem uma parte interessante onde diz para dividir a faixa de rodagem em regiões, afim de conseguir minimizar processamento computacional._**

---
4. [**Artigo**] - [Processamento de Imagens: Métodos e Análises](http://www.cbpf.br/cat/pdsi/pdf/ProcessamentoImagens.PDF)
	
	>"Neste artigo procuramos dar uma visão da área de processamento digital de imagens e suas aplicações. Abordamos conceitos importantes sobre a representação espacial de um pixel, a **medida de distâncias**, a segmentação de uma imagem e o reconhecimento de formas. Utilizamos situações reais para exemplificarmos as técnicas apresentadas. É nosso objetivo **abordar de forma introdutória e simplificada o tema**.¨

---
5. [**Artigo**, 2014] - [Mensuração da velocidade de deslocamento de corpos rígidos em tempo real por análise de sequência de imagens e pela transformação empírica baseada nas funções polinomiais](http://seer.upf.br/index.php/rbca/article/download/2857/2556)

	>"Resumo: Este trabalho apresenta uma metodologia para mensurar a velocidade de um corpo rígido em movimento por meio da análise de sequências de imagens adquiridas por uma filmadora digital comercial. ... Esse resultado é obtido pela aplicação da técnica de segmentação **baseada na média temporal dos valores de brilho de cada pixel registrado em N quadros de imagens consecutivos**. Após a detecção e a segmentação dos corpos em movimento, alguns pontos dispostos sobre as suas imagens (pontos do espaço-imagem) são transformados em coordenadas métricas do espaço-objeto. ... Transformando os pontos desejados do plano-imagem (2D) para seus respectivos correspondentes no espaço-objeto (3D), a distância percorrida pelo corpo em um determinado intervalo de tempo pode ser calculada e, dessa forma, a velocidade de deslocamento do corpo é mensurada."

---
6. [**Artigo**, UTFPR, 2016] - [A Video-Based System for Vehicle Speed Measurment in Urban Roadways	](http://www.dainf.ct.utfpr.edu.br/~rminetto/projects/vehicle-speed/Paper_ITS_final.pdf)  
**[10/07 - Broch] _- Bem interessante, apresenta toda a metodologia de como funciona o radar e depois compara os resultados com um radar de Loop já instalado. Foi feito por professores da UTFPR de Curitiba. Nesse [SITE](http://www.dainf.ct.utfpr.edu.br/~rminetto/projects/vehicle-speed/) está disponível o DATASET e Códigos utilizados._**

	>"In this paper, we propose a non-intrusive, **videobased system for vehicle speed measurement** in urban roadways. Our system uses an optimized motion detector and a novel text detector to efficiently locate vehicle license plates in image regions containing motion. Distinctive features are then selected on the license plate regions, tracked across multiple frames, and rectified for perspective distortion. Vehicle speed is measured by comparing the trajectories of the tracked features to known real world measures. The proposed system was tested on a data set containing approximately five hours of videos recorded in different weather conditions by a single low-cost camera, ... . **The measured speeds have an average error of -0.5 km/h, staying inside the [-3,+2] km/h limit determined by regulatory authorities**..."

---
## IV - TCCs

1. [**TCC**, 53 pág., 2016] - [Robô móvel com visão computacional usando a **biblioteca OpenCV** para seguimento de linha](http://www.cear.ufpb.br/arquivos/cgee/TCC/TCC_-_PEDRO_HENRIQUE_MEIRA_DE_ANDRADE.pdf)

	>" A plataforma utilizada é um pequeno robô móvel e dotado de uma câmera, capaz de seguir uma linha no chão. O controle cinemático é implementado em uma Raspberry Pi que também é responsável pelo processamento da imagem. A grande vantagem dessa metodologia é que com a câmera o robô pode adiantar prováveis curvas e alterar a velocidade e posição conforme a trajetória, tornando o movimento mais eficaz. Foi utilizada a **biblioteca OpenCV** que é a base para todo o tratamento da imagem e por consequência, do controle de velocidade e direção. O **acionamento dos motores** e a leitura dos sensores foram feitos usando a plataforma Arduino interligado a Raspberry Pi.

---
## V - Tutoriais e Projetos

1. [**Tutorial**, 2017] - [Object Tracking using OpenCV (C++/Python)](https://www.learnopencv.com/object-tracking-using-opencv-cpp-python/)

	>In this tutorial, we will learn about **OpenCV tracking API** that was introduced in OpenCV 3.0. We will learn **how and when to use the 6 different trackers available in OpenCV 3.2** — BOOSTING, MIL, KCF, TLD, MEDIANFLOW, and GOTURN. We will also learn the general theory behind modern tracking algorithms.

---
2. [**Tutorial**, 2016] - [Real-time speed estimation of cars with OpenCV](https://www.amphioxus.org/content/real-time-speed-estimation-cars)  
**[10/07 - Broch] _- Apresenta a um forma de medir velocidade utilizando a biblioteca OpenCV C++. Não é tão passo a passo, mas apresenta alguns fluxogramas de como é o funcionamento. Tem os códigos no [BitBucket](https://bitbucket.org/amphioxus/vehicletracker3)._**

---
3. [**Tutorial**, 2015] - [Basic motion detection and tracking with Python and OpenCV Python](https://www.pyimagesearch.com/2015/05/25/basic-motion-detection-and-tracking-with-python-and-opencv/)  
**[11/07 - Broch] _- Pode ser bem útil para entender melhor e já começar testando. Apresenta a um  passo a passo de como utilizar o motion detection e tracking. Tem os códigos no explicados_**

	
	**[11/07 - Broch] _- Esse site [www.pyimagesearch.com](https://www.pyimagesearch.com/) é bom, tem vários tutoriais, a maioria tudo relacionado a processamento de imagem utilizando a bib OpenCV em Python._**

---
4. [**Projeto Github**, 2016] - [**Speedtrack** - Python + OpenCV tool to count cars on the road in front of my house](https://github.com/iandees/speedtrack)

	>"Capture a frame of RGB video from the webcam. Convert it to HSV and pick out only the Value channel to convert to grayscale. After converting to grayscale, apply a blur function and add the frame to the running average of the scene."

	>**Prior Art and Helpful Information**
	>- Kyle Hounslow has an excellent set of YouTube tutorials on OpenCV. His [tutorial on Method of Sequential Images](https://www.youtube.com/watch?v=X6rPdRZzgjg) was a big help in getting started.  
	>- Claude Paeau's [YouTube video](https://www.youtube.com/watch?v=eRi50BbJUro) on motion tracking in his front yard was what got me started down this road. His code walkthrough helped me get started.

---
## VI - Livros

1. [**Livro**, 1999] - [Processamento Digital de Imagem](http://www.ogemarques.com/wp-content/uploads/2014/11/pdi99.pdf)


