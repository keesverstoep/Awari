#
# Copyright 2024 Vrije Universiteit Amsterdam
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

binomium = [[0],
[0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[0,0,0,0,0,0,0,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49],
[0,0,0,0,0,0,0,0,1,3,6,10,15,21,28,36,45,55,66,78,91,105,120,136,153,171,190,210,231,253,276,300,325,351,378,406,435,465,496,528,561,595,630,666,703,741,780,820,861,903,946,990,1035,1081,1128,1176,1225],
[0,0,0,0,0,0,0,0,1,4,10,20,35,56,84,120,165,220,286,364,455,560,680,816,969,1140,1330,1540,1771,2024,2300,2600,2925,3276,3654,4060,4495,4960,5456,5984,6545,7140,7770,8436,9139,9880,10660,11480,12341,13244,14190,15180,16215,17296,18424,19600,20825],
[0,0,0,0,0,0,0,0,1,5,15,35,70,126,210,330,495,715,1001,1365,1820,2380,3060,3876,4845,5985,7315,8855,10626,12650,14950,17550,20475,23751,27405,31465,35960,40920,46376,52360,58905,66045,73815,82251,91390,101270,111930,123410,135751,148995,163185,178365,194580,211876,230300,249900,270725],
[0,0,0,0,0,0,0,0,1,6,21,56,126,252,462,792,1287,2002,3003,4368,6188,8568,11628,15504,20349,26334,33649,42504,53130,65780,80730,98280,118755,142506,169911,201376,237336,278256,324632,376992,435897,501942,575757,658008,749398,850668,962598,1086008,1221759,1370754,1533939,1712304,1906884,2118760,2349060,2598960,2869685],
[0,0,0,0,0,0,0,0,1,7,28,84,210,462,924,1716,3003,5005,8008,12376,18564,27132,38760,54264,74613,100947,134596,177100,230230,296010,376740,475020,593775,736281,906192,1107568,1344904,1623160,1947792,2324784,2760681,3262623,3838380,4496388,5245786,6096454,7059052,8145060,9366819,10737573,12271512,13983816,15890700,18009460,20358520,22957480,25827165],
[0,0,0,0,0,0,0,0,1,8,36,120,330,792,1716,3432,6435,11440,19448,31824,50388,77520,116280,170544,245157,346104,480700,657800,888030,1184040,1560780,2035800,2629575,3365856,4272048,5379616,6724520,8347680,10295472,12620256,15380937,18643560,22481940,26978328,32224114,38320568,45379620,53524680,62891499,73629072,85900584,99884400,115775100,133784560,154143080,177100560,202927725],
[0,0,0,0,0,0,0,0,1,9,45,165,495,1287,3003,6435,12870,24310,43758,75582,125970,203490,319770,490314,735471,1081575,1562275,2220075,3108105,4292145,5852925,7888725,10518300,13884156,18156204,23535820,30260340,38608020,48903492,61523748,76904685,95548245,118030185,145008513,177232627,215553195,260932815,314457495,377348994,450978066,536878650,636763050,752538150,886322710,1040465790,1217566350,1420494075],
[0,0,0,0,0,0,0,0,1,10,55,220,715,2002,5005,11440,24310,48620,92378,167960,293930,497420,817190,1307504,2042975,3124550,4686825,6906900,10015005,14307150,20160075,28048800,38567100,52451256,70607460,94143280,124403620,163011640,211915132,273438880,350343565,445891810,563921995,708930508,886163135,1101716330,1362649145,1677106640,2054455634,2505433700,3042312350,3679075400,4431613550,5317936260,6358402050,7575968400,8996462475],
[0,0,0,0,0,0,0,0,1,11,66,286,1001,3003,8008,19448,43758,92378,184756,352716,646646,1144066,1961256,3268760,5311735,8436285,13123110,20030010,30045015,44352165,64512240,92561040,131128140,183579396,254186856,348330136,472733756,635745396,847660528,1121099408,1471442973,1917334783,2481256778,3190187286,4076350421,5178066751,6540715896,8217822536,10272278170,12777711870,15820024220,19499099620,23930713170,29248649430,35607051480,43183019880,52179482355],
]