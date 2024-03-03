# paradox-planetary-gearbox-optimization

(English follows)
下記論文に基づいて不思議遊星歯車減速機構の最適パラメータを計算するスクリプトです．
https://www.jstage.jst.go.jp/article/kikaic1979/62/596/62_596_1548/_article

以下各ギアをA～Dと呼称します
A:サンギア
B:遊星ギア
C:リングギア(固定)
D:リングギア(出力軸)

#使用方法
以下のパラメータを設定します．
1.ギアのモジュール
2.各ギアの歯数
3.各ギアの圧力角
4.ギアA,B,Dの噛み合い率
　(※ただしギアAの噛み合い率は影響のない範囲で小さい値を設定したほうが全体としての効率がよくなると論文中に記載があるので注意)
5.ギアB,Dの転位係数

必要に応じてパラメータ上に記載の条件も変更してください．特に
sk:歯先の限界厚さ=転位すると歯先とがりが生ずるが，強度その他諸々の都合で歯先の厚みの限界値を設定したい場合
は必要に応じて設定してください．残りはあまり大きな影響はないです．

上記設定後スクリプトを実行してください．
出力としては基本的にギアA,Cの転位係数ですが，その後CAD作図するのに必要になるため各ギアの転位係数とかみ合いピッチ円半径が出力されます．

paradox planetary gearbox optimization using below article.

https://www.jstage.jst.go.jp/article/kikaic1979/62/596/62_596_1548/_article

※gear A is sun gear, B is planetary gear, C is fixed ring gear and D is moving ring gear.

Set following parameters
1. module of gear
2. Number of teeth on each gear
3. plessure angle of each gears
4. tooth contact ratio of gear B, D and A
   (※it is recommended that contact ratio of gear A should be smaller as much as possible)
5. addendum modification coefficient of gear B and D

Please change the conditions listed above the parameters as necessary.
Especially,
sk:the limit of gear teeth thickness
should be modified if you need. other conditions will affect the results little.

And run the script.

Returns of this script is addendum modification coefficient of gear A and C.
However addendum modification coefficient and operating pitch radius of all gears appears on the console because these values need for CAD drawings.
