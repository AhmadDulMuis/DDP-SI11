{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyOom4Q/BLnUlHPR8nRNyQ5D"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","source":["numbers = [\n","951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,  615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,  386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,  399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527\n","]\n","print(numbers[1])\n","i = 0\n","while i < len(numbers):\n","    if numbers[i] % 2 == 1:\n","        print(numbers[i])\n","    if numbers[i] == 5533:\n","        break\n","    i += 1"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"JwrlrDfykc3Z","executionInfo":{"status":"ok","timestamp":1730277407174,"user_tz":-420,"elapsed":434,"user":{"displayName":"Gaming Proplayer","userId":"12588710889172713693"}},"outputId":"c5ed1aa8-f332-44c8-cccd-a37c3cc9d565"},"execution_count":9,"outputs":[{"output_type":"stream","name":"stdout","text":["402\n","951\n","651\n","69\n","319\n","601\n","485\n","507\n","725\n","547\n","615\n","83\n","165\n","141\n","501\n","263\n","617\n","865\n","575\n","219\n","105\n","941\n","47\n","907\n","375\n","823\n","597\n","615\n","953\n","345\n","399\n","219\n","237\n","949\n","687\n","217\n","815\n","67\n","767\n","553\n","81\n","379\n","843\n","831\n","445\n","717\n","609\n","451\n","753\n","685\n","93\n","857\n","721\n","753\n","743\n","527\n"]}]},{"cell_type":"code","source":["hasil = 0\n","for i in range(1,20,2):\n","    hasil += i\n","print(\"1+3+5+7+9+11+13+15+17+19={hasil}\")"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"07a1zglTkiIK","executionInfo":{"status":"ok","timestamp":1730277443569,"user_tz":-420,"elapsed":431,"user":{"displayName":"Gaming Proplayer","userId":"12588710889172713693"}},"outputId":"c0d2094e-aa70-4545-e277-aa60cec5e099"},"execution_count":10,"outputs":[{"output_type":"stream","name":"stdout","text":["1+3+5+7+9+11+13+15+17+19={hasil}\n"]}]},{"cell_type":"code","source":["b = int(input(\"Masukan jumlah baris : \"))\n","for y in range(1, b+1):\n","    print(\"*\" * y)"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"P0pdiSI8h00z","executionInfo":{"status":"ok","timestamp":1730277056827,"user_tz":-420,"elapsed":5125,"user":{"displayName":"Gaming Proplayer","userId":"12588710889172713693"}},"outputId":"e89774a9-f663-4951-d102-539dedf1b374"},"execution_count":null,"outputs":[{"output_type":"stream","name":"stdout","text":["Masukan jumlah baris : 5\n","*\n","**\n","***\n","****\n","*****\n"]}]}]}