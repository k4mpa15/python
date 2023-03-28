import string

message = "LEWFIKLERKVCP, KYV NZUVJGIVRU RUFGKZFE FW SCLVKFFKY WLETKZFERCZKP RCJF TFDVJ NZKY KYVGIVMRCVETV FW SCLVKFFKY JVTLIZKP IZJBJ. WRI KFF CZKKCV YRJ SVVE UFEV FMVI KYV PVRIJ KF VEJLIV KYV JVTLIZKP FW R SCLVKFFKY TFEEVTKZFE.JFDV VORDGCVJ FW SCLVKFFKY JVTLIZKP IZJBJ RIV DRE ZE KYV DZUUCV RKKRTBJ (ZEKVITVGKZEX REU KYVE TYREXZEX TFDDREUJ), ZUVEKZKP KIRTBZEX, ZEKVITVGKZEX ZEWFIDRKZFE, UZJILGKZFE FW R UVMZTV’J FGVIRKZFEJ, REU GRJJZMV VRMVJUIFGGZEX.NYZCV DFJK GVFGCV KYZEB PFLI YVRIK IRKV FI DLJZT GIVWVIVETVJ RIVE’K KYRK ZDGFIKREK, SVJKGIRTKZTVJ WFI SCLVKFFKY JVTLIZKP JYFLCU RCNRPJ SV VEXRXVU, RJ VRMVJUIFGGZEX (FI LERLKYFIZQVU WZCDZEX) TFLCU YRGGVE ULIZEX RE ZDGFIKREK, FI JVTLIV, GYFEV TRCC DRUV KYIFLXY RE FCUVI SCLVKFFKY JGVRBVI.ZE WRTK, KYFLXY KYV ZEKVIEVK FW KYZEXJ ZJ JKIZMZEX KFNRIUJ DRBZEX FLI VMVIPURP CZWV VRJZVI, KYVIV ZJ RE VMVI-XIFNZEX GIVJVETV FW KYV ZEKVIEVK FW VMZC KYZEXJ."
mode = 'encrypt'
SYMBOLS = string.ascii_lowercase
for key in range(0,25):
    translated = ''

    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            
            if mode == 'encrypt':
                translatedIndex = symbolIndex + key
            elif mode == 'descrypt':
                translatedIndex = symbolIndex - key
            
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)
                
            translated = translated + SYMBOLS[translatedIndex]
            
        else:
            translated = translated + symbol
            
    print(translated)
            