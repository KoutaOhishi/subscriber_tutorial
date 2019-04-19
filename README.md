# subscriber_tutorial

## Setup
```
cd ~/catkin_ws/src/

git clone

cd subscriber_tutorial/

chmod 755 src/*

cd ~/catkin_ws/

catkin_make
```

## Tutorial
### section 1
基本的なsubscriberの使い方を学ぶ。  

端末を立ち上げて以下のコマンドを実行する。
```
roslaunch subscriber_tutorial section_1.launch
```  


別の端末を立ち上げて、以下のコマンドを実行し、現在masterに登録されているトピックを確認する。
```
rostopic list

#実行結果
/rosout
/rosout_agg
/subscriber_tutorial/encryption ←今回使うトピック
```

"/subscriber_tutorial/encryption"の型を確認する。  
以下のコマンドを実行する。
```
rostopic type /subscriber_tutorial/encryption

#実行結果
std_msgs/String
```
プログラミングでsubscriberを書く際、メッセージの型が合ってないとsubscribeすることができないので注意!

"/subscriber_tutorial/encryption"の中身を確認する。  
以下のコマンドを実行する。
```
rostopic echo /subscriber_tutorial/encryption

#実行結果
data: "Pubv Ynobengbel"
---
data: "Grnz FBOVGF"
---
data: "Fbxn Havirefvgl"
---
...
```
確認が出来たら**ctrl + c**で停止させる。  
"/subscriber_tutorial/encryption"の*data*という変数に、文字列が格納されている。

#### Let's coding!
この文字列はシーザー暗号になってます。  
文字列をsubscribeして、解読するプログラムをpythonで書いてみましょう。  
シーザー暗号を解読する関数は用意してます。  
src/section_1.pyにプログラムを書いてみてください。

---


### section 2
複数の変数を持ったトピックを扱えるようにする。  
すべての端末を切った後、以下のコマンドを実行する。
```
roslaunch subscriber_tutorial section_2.launch
```

別の端末を立ち上げて、どんなトピックがpublishされているかを確認をする。
```
rostopic list

#実行結果
/rosout
/rosout_agg
/subscriber_tutorial/formula ←今回使うのはこれ！
```
トピックの型を確認する。
```
rostopic type /subscriber_tutorial/formula

#実行結果
subscriber_tutorial/Formula
```
トピックの中身を確認する。
```
rosmsg show subscriber_tutorial/Formula

#実行結果
int32 item_1
int32 item_2
string operators
```
```
rostopic echo /subscriber_tutorial/formula

#実行結果
item_1: 89
item_2: -41
operators: "-"
---
item_1: -28
item_2: -4
operators: "/"
---
item_1: -74
item_2: -79
operators: "/"
---
...
```

item_1とitem_2にはランダムでint型の数値が入り、  
operatorsにはstring型で演算子**（+,-,*,/）**が入っている。

### Let's coding!
"/subscriber_tutorial/formula"をsubscribeして、  
item_1とitem_2をoperatorsの演算子に従って計算して、その結果を表示させてください。
##### 例） (89) - (-41) = 130

---
## Section 3
複数のトピックをsubscribeして、処理を行えるようにする。

すべての端末を切った後、以下のコマンドを実行する。  
```
roslaunch subscriber_tutorial section_3.launch
```

別の端末を立ち上げて、どんなトピックがpublishされているかを確認する。
```
rostopic list

#実行結果
/rosout
/rosout_agg
/subscriber_tutorial/item_1
/subscriber_tutorial/item_2
/subscriber_tutorial/operators
```

今回使うのは、次の３つのトピック  
- "/subscriber_tutorial/item_1"
- "/subscriber_tutorial/item_2"
- "/subscriber_tutorial/operators"


それぞれのトピックの型は、
```
rostopic type /subscriber_tutorial/item_1

#実行結果
std_msgs/Int32
```
```
rostopic type /subscriber_tutorial/item_2

#実行結果
std_msgs/Int32
```
```
rostopic type /subscriber_tutorial/operators

#実行結果
std_msgs/String
```

それぞれのトピックの中身は、
```
rostopic echo /subscriber_tutorial/item_1

#実行結果
data: 46
---
data: 89
---
data: -99
---
```
```
rostopic echo /subscriber_tutorial/item_2

#実行結果
data: -41
---
data: -34
---
data: 72
---
```
```
rostopic echo /subscriber_tutorial/operators

#実行結果
data: "-"
---
data: "+"
---
data: "-"
---
```
それぞれのトピックは、*data* という変数の中に値が格納されている。  
section 2では、１つのトピックの中に、３つの変数が入っていたが、今回は、トピックが３つある。  

### Let's coding!
3つのトピックをsubscribeして、  
"/subscriber_tutorial/item_1"の値と、"/subscriber_tutorial/item_2"の値を、  
"/subscriber_tutorial/operators"の演算子に従って計算してください。
