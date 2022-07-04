1. log file 轉檔:
	python3 .\parseTxt.py L:\\PRG\nodejs\\ABBA\\現場log\\20220621\\log\\RFIDAtag_20220621.log

	python3 .\abbatecDraw\parseTxt.py RFIDAtagAAAAAAtest-1.log

	python3 .\abbatecDraw\parseTxt.py RFIDAtagout3.log
	python3 .\abbatecDraw\parseTxt.py RFIDAtagin3.log
	python3 .\abbatecDraw\parseTxt.py RFIDAtagAAAAAAtest-2.log
	python3 .\abbatecDraw\parseTxt.py RFIDAtag_20220701-1.log


output: RFIDAtag_20220621after.log


2. 安裝套件: 
		python3 -m pip install numpy
		python3 -m pip install matplotlib

2. 繪圖輸出
	python3 .\drawTagTrace.py L:\\PRG\nodejs\\ABBA\\現場log\\20220621\\log\\RFIDAtag_20220621after.log

	python3 .\abbatecDraw\drawTagTrace.py RFIDAtagAAAAAAtestafter-1.log

	python3 .\abbatecDraw\drawTagTrace.py RFIDAtagAAAAAAtestafter-1.log


	python3 .\abbatecDraw\drawTagTrace.py RFIDAtagout3after.log
	python3 .\abbatecDraw\drawTagTrace.py RFIDAtagin3after.log
	python3 .\abbatecDraw\drawTagTrace.py RFIDAtagAAAAAAtest-2after.log
 	python3 .\abbatecDraw\drawTagTrace.py RFIDAtag_20220704after.log