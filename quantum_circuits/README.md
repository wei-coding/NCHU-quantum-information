# Quantum Circuit Simulator

## 執行方式

```shell=
pip install -r requirements.txt
flask run
```

或是直接使用docker版本

```shell=
docker run -it weisdocker0830/quantum_simulator -p 5000:5000
```

於瀏覽器中直接開啟 http://localhost:5000 即可看到GUI

## 說明

每一行代表一個邏輯閘，以空格分隔在每個bit上的作用元件
其中:

+ 0為低位啟動控制
+ 1為高位啟動控制
+ 2為NOT Gate
+ 3為不做任何控制

例如:
1 1 2
即為由bit 0和bit 1高位啟動控制bit 2的CNOT gate

於Gates框內輸入上述格式的字串後按下`開始計算`即可輸出真值表，程式內建格式檢查
清除按下`清除所有結果`即可