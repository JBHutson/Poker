cardVals = [
	'2',
	'3',
	'4',
	'5',
	'6',
	'7',
	'8',
	'9',
	'10',
	'J',
	'Q',
	'K',
	'A',
	]

suits = [
	'♠',
	'♥',
	'♣',
	'♦'
	]

suitVals = [
	'S',
	'H',
	'C',
	'D'
	]


cardRanks = {
	'2': 1,
	'3': 2,
	'4': 3,
	'5': 4,
	'6': 5,
	'7': 6,
	'8': 7,
	'9': 8,
	'10': 9,
	'J': 10,
	'Q': 11,
	'K': 12,
	'A': 13
	}

playerNumChoices = [
 		'10 Players',
		'9 Players',
 		'8 Players',
		'7 Players',
 		'6 Players',
		'5 Players',
 		'4 Players',
 		'3 Players',
		'2 Players'
		]

cardChoices = [
	'Hole 1',
	'Hole 2',
	'Flop 1',
	'Flop 2',
	'Flop 3',
	'Turn',
	'River'
	]

tenPlayerHoleWinOdds = {
		'AA_P': .3136,
		'KK_P': .2643,
		'QQ_P': .2266,
		'AK_S': .2173,
		'JJ_P': .1984,
		'AQ_S': .2044,
		'KQ_S': .198,
		'AJ_S': .1951,
		'KJ_S': .1894,
		'A10_S': .1887,
		'QJ_S': .1855,
		'AK_U': .1829,
		'1010_P': .1776,
		'K10_S': .1834,
		'Q10_S': .1804,
		'J10_S': .1807,
		'99_P': .1605,
		'AQ_U': .1678,
		'A9_S': .1687,
		'KQ_U': .163,
		'K9_S': .1622,
		'109_S': .1633,
		'A8_S': .1634,
		'J9_S': .1589,
		'Q9_S': .1589,
		'88_P': .1496,
		'A5_S': .1623,
		'AJ_U': .157,
		'A7_S': .1593,
		'A4_S': .1588,
		'A3_S': .1551,
		'KJ_U': .153,
		'A6_S': .1562,
		'QJ_U': .1507,
		'77_P': .1414,
		'A2_S': .1502,
		'K8_S': .1503,
		'108_S': .1505,
		'98_S': .1469,
		'A10_U': .1493,
		'J8_S': .1466,
		'Q8_S': .1461,
		'K7_S': .1464,
		'K10_U': .146,
		'J10_U': .1464,
		'66_P': .1351,
		'Q10_U': .1445,
		'K6_S': .1435,
		'87_S': .1403,
		'K5_S': .1409,
		'97_S': .1381,
		'55_P': .1288,
		'107_S': .1382,
		'K4_S': .1378,
		'76_S': .1354,
		'44_P': .1256,
		'K3_S': .1349,
		'Q7_S': .1357,
		'J7_S': .1349,
		'33_P': .1231,
		'K2_S': .1321,
		'22_P': .1215,
		'86_S': .132,
		'65_S': .1314,
		'Q6_S': .1328,
		'54_S': .1288,
		'Q5_S': .1305,
		'75_S': .1273,
		'96_S': .1274,
		'109_U': .1287,
		'Q4_S': .1273,
		'106_S': .1272,
		'A9_U': .1274,
		'Q3_S': .1244,
		'64_S': .1222,
		'J6_S': .1256,
		'Q2_S': .1217,
		'J9_U': .1236,
		'85_S': .1216,
		'53_S': .1197,
		'K9_U': .1227,
		'J5_S': .1232,
		'Q9_U': .1211,
		'J4_S': .1201,
		'A8_U': .1216,
		'74_S': .1159,
		'J3_S': .1174,
		'43_S': .1136,
		'95_S': .117,
		'J2_S': .1147,
		'105_S': .1184,
		'A5_U': .12,
		'63_S': .1109,
		'104_S': .1153,
		'A7_U': .1171,
		'108_U': .1148,
		'103_S': .1124,
		'A4_U': .1163,
		'98_U': .112,
		'84_S': .1104,
		'52_S': .1083,
		'102_S': .1098,
		'A3_U': .1122,
		'42_U': .1047,
		'A6_U': .1135,
		'94_S': .1073,
		'J8_U': .1094,
		'K8_U': .1097,
		'73_S': .1046,
		'93_S': .1042,
		'87_U': .1057,
		'Q8_U': .107,
		'A2_U': .107,
		'32_S': .099,
		'92_S': .1015,
		'62_S': .0996,
		'K7_U': .1054,
		'83_S': .1007,
		'97_U': .1024,
		'76_U': .101,
		'82_S': .0978,
		'107_U': .1017,
		'K6_U': .1019,
		'72_S': .0953,
		'65_U': .0973,
		'86_U': .0967,
		'K5_U': .0993,
		'54_U': .0949,
		'J7_U': .0966,
		'K4_U': .0958,
		'Q7_U': .0957,
		'75_U': .0926,
		'K3_U': .0926,
		'96_U': .0909,
		'K2_U': .0897,
		'Q6_U': .0925,
		'64_U': .0875,
		'Q5_U': .09,
		'106_U': .0898,
		'53_U': .0852,
		'85_U': .086,
		'Q4_U': .0867,
		'J6_U': .0865,
		'Q3_U': .0835,
		'43_U': .079,
		'74_U': .0805,
		'Q2_U': .0806,
		'J5_U': .0841,
		'95_U': .0799,
		'J4_U': .0807,
		'63_U': .0756,
		'J3_U': .0775,
		'105_U': .0806,
		'52_U': .0734,
		'J2_U': .0748,
		'104_U': .0771,
		'84_U': .0738,
		'42_U': .0696,
		'103_U': .074,
		'102_U': .0711,
		'73_U': .0685,
		'94_U': .0696,
		'32_U': .0635,
		'62_U': .0638,
		'93_U': .0663,
		'92_U': .0635,
		'83_U': .0636,
		'82_U': .0606,
		'72_U': .0586
		}


eightPlayerHoleWinOdds = {
		'AA_P': .3905,
		'KK_P': .3326,
		'QQ_P': .2871,
		'AK_S': .26,
		'JJ_P': .2513,
		'AQ_S': .2451,
		'KQ_S': .2372,
		'AJ_S': .2341,
		'1010_P': .2232,
		'AK_U': .2268,
		'KJ_S': .2266,
		'A10_S': .2255,
		'QJ_S': .221,
		'K10_S': .2187,
		'Q10_S': .2138,
		'J10_S': .2126,
		'AQ_U': .2098,
		'99_P': .1989,
		'KQ_U': .2031,
		'A9_S': .2028,
		'AJ_U': .197,
		'K9_S': .195,
		'A8_S': .1966,
		'KJ_U': .191,
		'88_P': .1819,
		'109_S': .1918,
		'Q9_S': .1903,
		'J9_S': .1896,
		'A5_S': .1929,
		'A7_S': .1912,
		'QJ_U': .1867,
		'A10_U': .1874,
		'A4_S': .1886,
		'A6_S': .1862,
		'A3_S': .1841,
		'K10_U': .1818,
		'K8_S': .1805,
		'77_P': .1685,
		'Q10_U': .1783,
		'J10_U': .1786,
		'A2_S': .1786,
		'108_S': .1768,
		'Q8_S': .1751,
		'J8_S': .1744,
		'K7_S': .1757,
		'98_S': .1731,
		'K6_S': .1717,
		'66_P': .1584,
		'K5_S': .1683,
		'87_S': .1638,
		'K4_S': .1644,
		'97_S': .162,
		'107_S': .163,
		'Q7_S': .1622,
		'A9_U': .1627,
		'J7_S': .1607,
		'K3_S': .1606,
		'55_P': .1493,
		'76_S': .1566,
		'K2_S': .157,
		'Q6_S': .1585,
		'109_U': .1571,
		'K9_U': .1562,
		'86_S': .1537,
		'Q5_S': .1556,
		'44_P': .1431,
		'J9_U': .1534,
		'65_S': .1512,
		'Q9_U': .1527,
		'A8_U': .1555,
		'Q4_S': .1516,
		'96_S': .1499,
		'54_S': .1474,
		'106_S': .1503,
		'33_P': .1383,
		'75_S': .1474,
		'Q3_S': .1481,
		'J6_S': .1492,
		'22_P': .1349,
		'Q2_S': .1446,
		'A5_U': .151,
		'A7_U': .1494,
		'J5_S': .1466,
		'64_S': .1407,
		'85_S': .1422,
		'J4_S': .1428,
		'A4_U': .1463,
		'53_S': .1371,
		'J3_S': .1392,
		'A6_U': .1439,
		'108_U': .1407,
		'K8_U': .1401,
		'95_S': .1381,
		'105_S': .1398,
		'A3_U': .1415,
		'98_U': .1373,
		'J2_S': .1359,
		'74_S': .1348,
		'J8_U': .1368,
		'104_S': .1364,
		'Q8_U': .136,
		'43_S': .1309,
		'103_S': .133,
		'A2_U': .1354,
		'K7_U': .1348,
		'63_S': .1285,
		'84_S': .1298,
		'102_S': .1295,
		'52_S': .125,
		'87_U': .1279,
		'94_S': .1271,
		'K6_U': .1302,
		'42_S': .1208,
		'73_S': .1225,
		'93_S': .1237,
		'97_U': .1254,
		'107_U': .1255,
		'92_S': .1203,
		'K5_U': .1265,
		'76_U': .1208,
		'83_S': .1188,
		'32_S': .1149,
		'62_S': .1162,
		'Q7_U': .1222,
		'J7_U': .1218,
		'K4_U': .1221,
		'82_S': .1157,
		'86_U': .117,
		'K3_U': .1179,
		'65_U': .1151,
		'Q6_U': .1181,
		'72_S': .1119,
		'K2_U': .1141,
		'54_U': .1112,
		'96_U': .1122,
		'Q5_U': .1146,
		'75_U': .1107,
		'106_U': .1118,
		'Q4_U': .1103,
		'J6_U': .1094,
		'64_U': .1039,
		'Q3_U': .1063,
		'85_U': .1047,
		'J5_U': .1064,
		'Q2_U': .1026,
		'53_U': .1004,
		'J4_U': .1022,
		'95_U': .0997,
		'74_U': .0973,
		'105_U': .1006,
		'J3_U': .0983,
		'43_U': .0938,
		'J2_U': .0946,
		'104_U': .0966,
		'63_U': .0908,
		'84_U': .0912,
		'103_U': .0928,
		'52_U': .0873,
		'102_U': .0893,
		'94_U': .0876,
		'42_U': .083,
		'73_U': .0841,
		'93_U': .084,
		'92_U': .0804,
		'32_U': .0767,
		'62_U': .0779,
		'83_U': .0796,
		'82_U': .0761,
		'72_U': .0728
		}

sixPlayerHoleWinOdds = {
		'AA_P': .4951,
		'KK_P': .4332,
		'QQ_P': .383,
		'JJ_P': .3405,
		'AK_S': .3215,
		'1010': .3044,
		'AQ_S': .3056,
		'KQ_S': .2955,
		'AJ_S': .2928,
		'AK_U': .2896,
		'KJ_S': .2828,
		'A10_S': .2827,
		'99_P': .2711,
		'QJ_S': .2757,
		'AQ_U': .2721,
		'K10_S': .2732,
		'Q10_S': .2664,
		'KQ_U': .2628,
		'J10_S': .2633,
		'AJ_U': .2579,
		'A9_S': .2575,
		'88_P': .2451,
		'KJ_U': .2488,
		'K9_S': .2473,
		'A8_S': .2498,
		'A10_U': .2466,
		'QJ_U': .2426,
		'Q9_S': .2407,
		'A7_S': .2427,
		'109_S': .239,
		'J9_S': .2382,
		'K10_U': .238,
		'A5_S': .2419,
		'77_P': .2235,
		'Q10_U': .232,
		'A4_S': .2363,
		'A6_S': .235,
		'J10_U': .2303,
		'K8_S': .2297,
		'A3_S': .2305,
		'Q8_S': .2224,
		'K7_S': .2237,
		'A2_S': .2239,
		'108_S': .2212,
		'J8_S': .2201,
		'98_S': .2172,
		'A9_U': .2193,
		'66_P': .2059,
		'K6_S': .2175,
		'K5_S': .2129,
		'K9_U': .2098,
		'A8_U': .2107,
		'Q7_S': .2065,
		'K4_S': .2075,
		'87_S': .2039,
		'Q9_U': .2041,
		'107_S': .2046,
		'109_U': .2044,
		'97_S': .2030,
		'J7_S': .2038,
		'J9_U': .2028,
		'K3_S': .2025,
		'55_P': .1905,
		'Q6_S': .2019,
		'A7_U': .2025,
		'K2_S': .1976,
		'A5_U': .2015,
		'Q5_S': .1972,
		'76_S': .1931,
		'86_S': .1911,
		'Q4_S': .1922,
		'A4_U': .1951,
		'A6_U': .1943,
		'K8_U': .1904,
		'106_S': .1895,
		'96_S': .1882,
		'J6_S': .1892,
		'44_P': .1776,
		'Q3_S': .1869,
		'65_S': .1845,
		'A3_U': .1887,
		'108_U': .185,
		'J5_S': .1856,
		'Q8_U': .1843,
		'Q2_S': .1825,
		'J8_U': .1831,
		'75_S': .181,
		'98_U': .1814,
		'K7_U': .1838,
		'54_S': .1782,
		'J4_S': .1803,
		'A2_U': .1815,
		'85_S': .1773,
		'33_P': .1669,
		'J3_S': .1757,
		'105_S': .1762,
		'95_S': .1741,
		'K6_U': .1772,
		'64_S': .1717,
		'J2_S': .1711,
		'104_S': .1719,
		'22_P': .1587,
		'74_S': .1666,
		'53_S': .1659,
		'K5_U': .1718,
		'87_U': .1676,
		'103_S': .1672,
		'97_U': .1661,
		'107_U': .1671,
		'Q7_U': .167,
		'J7_U': .1651,
		'84_S': .1625,
		'102_S': .1627,
		'K4_U': .1659,
		'43_S': .159,
		'94_S': .1605,
		'63_S': .1577,
		'Q6_U': .1617,
		'K3_U': .1603,
		'93_S': .1567,
		'76_U': .1562,
		'52_S': .1519,
		'73_S': .1525,
		'92_S': .1522,
		'Q5_U': .1566,
		'K2_U': .1549,
		'86_U': .1535,
		'83_S': .1494,
		'42_S': .1468,
		'96_U': .15,
		'106_U': .1506,
		'Q4_U': .1508,
		'82_S': .1458,
		'65_U': .1471,
		'J6_U': .1494,
		'62_S': .1437,
		'32_S': .1402,
		'Q3_U': .1452,
		'75_U': .1434,
		'72_S': .1397,
		'J5_U': .1453,
		'54_U': .1405,
		'Q2_U': .14,
		'85_U': .1387,
		'J4_U': .1396,
		'64_U': .1334,
		'95_U': .1348,
		'105_U': .1363,
		'J3_U': .1342,
		'104_U': .1316,
		'J2_U': .1292,
		'53_U': .1271,
		'74_U': .1278,
		'103_U': .1262,
		'84_U': .1229,
		'43_U': .1199,
		'102_U': .1212,
		'63_U': .1182,
		'94_U': .1201,
		'93_U': .1158,
		'52_U': .1123,
		'73_U': .1124,
		'92_U': .1108,
		'42_U': .1067,
		'83_U': .1086,
		'62_U': .1032,
		'82_U': .1045,
		'32_U': .0998,
		'72_U': .0987
		}

fourPlayerHoleWinOdds = {
		'AA_P': .6418,
		'KK_P': .5859,
		'QQ_P': .5391,
		'JJ_P': .4963,
		'1010_P': .4569,
		'AK_S': .4252,
		'99_P': .4162,
		'AQ_S': .4107,
		'AK_U': .3966,
		'AJ_S': .3985,
		'KQ_S': .3941,
		'88_P': .3808,
		'A10_S': .3875,
		'AQ_U': .3811,
		'KJ_S': .3818,
		'QJ_S': .3702,
		'K10_S': .3712,
		'AJ_U': .3675,
		'KQ_U': .3642,
		'A9_S': .3618,
		'Q10_S': .3599,
		'77_P': .349,
		'A10_U': .3559,
		'J10_S': .3534,
		'KJ_U': .3508,
		'A8_S': .3532,
		'K9_S': .3453,
		'QJ_U': .3396,
		'A7_S': .3435,
		'K10_U': .3393,
		'Q9_S': .3341,
		'A5_S': .3389,
		'66_P': .3206,
		'A6_S': .3332,
		'Q10_U': .3283,
		'J9_S': .328,
		'A9_U': .3279,
		'A4_S': .3309,
		'109_S': .3255,
		'K8_S': .3251,
		'J10_U': .3224,
		'A3_S': .3231,
		'K7_S': .3177,
		'A8_U': .3183,
		'Q8_S': .3138,
		'K9_U': .3112,
		'A2_S': .3144,
		'J8_S': .3076,
		'K6_S': .3096,
		'55_P': .2947,
		'108_S': .3053,
		'A7_U': .308,
		'98_S': .3006,
		'Q9_U': .3004,
		'K5_S': .3026,
		'A5_U': .3025,
		'J9_U': .2946,
		'Q7_S': .2947,
		'109_U': .2928,
		'A6_U': .2966,
		'K4_S': .2949,
		'A4_U': .2936,
		'K8_U': .2893,
		'J7_S': .2881,
		'Q6_S': .2887,
		'107_S': .2859,
		'K3_S': .2877,
		'97_S': .2831,
		'87_S': .2828,
		'A3_U': .2849,
		'44_P': .2688,
		'Q5_S': .2817,
		'K7_U': .2814,
		'K2_S': .2805,
		'Q8_U': .2783,
		'J8_U': .2726,
		'Q4_S': .2743,
		'A2_U': .2756,
		'108_U': .271,
		'J6_S': .2702,
		'K6_U': .2725,
		'76_S': .2674,
		'106_S': .2676,
		'98_U': .2666,
		'86_S': .2662,
		'Q3_S': .2673,
		'96_S': .2652,
		'J5_S': .2652,
		'K5_U': .2647,
		'Q2_S': .2601,
		'33_P': .2456,
		'J4_S': .2579,
		'Q7_U': .2576,
		'65_S': .2536,
		'K4_U': .2565,
		'75_S': .2513,
		'J7_U': .2518,
		'J3_S': .2509,
		'105_S': .2507,
		'107_u': .2503,
		'85_S': .2489,
		'Q6_U': .2511,
		'87_U': .2477,
		'95_S': .2477,
		'97_U': .2476,
		'K3_U': .2484,
		'104_S': .2454,
		'J2_S': .2441,
		'54_S': .2433,
		'Q5_U': .2435,
		'64_S': .2374,
		'K2_U': .2405,
		'103_S': .2382,
		'22_P': .2251,
		'74_S': .2339,
		'Q4_U': .2354,
		'102_S': .2315,
		'84_S': .2313,
		'76_U': .2312,
		'J6_U': .2322,
		'94_S': .2305,
		'86_U': .2296,
		'106_U': .2303,
		'53_S': .2272,
		'96_U': .2282,
		'93_S': .2255,
		'Q3_U': .2275,
		'J5_U': .2267,
		'63_S': .22,
		'43_S': .219,
		'92_S': .2189,
		'Q2_U': .2199,
		'73_S': .2164,
		'J4_U': .2189,
		'65_U': .2167,
		'83_S': .2141,
		'75_U': .214,
		'52_S': .2103,
		'82_S': .2094,
		'85_U': .2111,
		'105_U': .2119,
		'J3_U': .2111,
		'95_U': .2093,
		'42_S': .2032,
		'54_U': .2058,
		'62_S': .2028,
		'104_U': .2061,
		'J2_U': .2035,
		'72_S': .1997,
		'64_U': .1993,
		'32_S': .1952,
		'103_U': .1984,
		'74_U': .1951,
		'84_U': .192,
		'102_U': .1909,
		'94_U': .1907,
		'53_U': .1886,
		'93_U': .1851,
		'63_U': .1806,
		'43_U': .1796,
		'92_U': .1778,
		'73_U': .1762,
		'83_U': .1736,
		'52_U': 1701,
		'82_U': .1683,
		'42_U': .1626,
		'62_U': .162,
		'72_U': .1583,
		'32_U': .1539
		}

threePlayerHoleWinOdds = {
		'AA_P': .7378,
		'KK_P': .6921,
		'QQ_P': .6529,
		'JJ_P': .6157,
		'1010_P': .5802,
		'99_P': .5408,
		'AK_S': .5177,
		'88_P': .5046,
		'AQ_S': .5056,
		'AK_U': .4928,
		'AJ_S': .4949,
		'KQ_S': .4828,
		'A10_S': .485,
		'AQ_U': .4801,
		'77_P': .4702,
		'KJ_S': .4722,
		'AJ_U': .4684,
		'K10_S': .4624,
		'A9_S': .4616,
		'KQ_U': .4561,
		'A10_U': .4579,
		'QJ_S': .4555,
		'A8_S': .4531,
		'66_P': .4377,
		'Q10_S': .4459,
		'KJ_U': .4446,
		'A7_S': .4432,
		'K9_S': .4388,
		'J10_S': .4344,
		'K10_U': .4342,
		'A9_U': .4325,
		'A5_S': .4349,
		'QJ_U': .4276,
		'A6_S': .4319,
		'Q9_S': .4225,
		'A4_S': .427,
		'A8_U': .4231,
		'Q10_U': .4173,
		'K8_S': .4191,
		'55_P': .407,
		'A3_S': .418,
		'J9_S': .4111,
		'K7_S': .4199,
		'A7_U': .4125,
		'K9_U': .4088,
		'J10_U': .4058,
		'A2_S': .4086,
		'109_S': .4038,
		'Q8_S': .4028,
		'K6_S': .4029,
		'A5_U': .4046,
		'A6_U': .4004,
		'Q9_U': .392,
		'K5_S': .3951,
		'J8_S': .3914,
		'A4_U': .3945,
		'K8_U': .3875,
		'44_P': .3742,
		'108_S': .3846,
		'K4_S': .3863,
		'Q7_S': .3833,
		'J9_U': .3805,
		'A3_U': .385,
		'K7_U': .3796,
		'98_S': .3774,
		'Q6_S': .377,
		'K3_S': .3778,
		'109_U': .3736,
		'J7_S': .3721,
		'Q8_U': .3709,
		'A2_U': .3747,
		'K6_U': .37,
		'K2_S': .3691,
		'Q5_S': .3693,
		'107_S': .3651,
		'J8_U': .3594,
		'97_S': .3595,
		'Q4_S': .3608,
		'K5_U': .3615,
		'87_S': .3565,
		'33_P': .3433,
		'108_U': .3526,
		'J6_S': .3533,
		'Q3_S': .3522,
		'Q7_U': .3501,
		'K4_U': .3519,
		'J5_S': .3479,
		'98_U': .3455,
		'106_S': .3464,
		'Q2_S': .344,
		'Q6_U': .3433,
		'96_S': .3408,
		'K3_U': .3426,
		'86_S': .3388,
		'J7_U': .3386,
		'76_S': .3385,
		'J4_S': .3395,
		'Q5_U': .3348,
		'107_U': .3319,
		'K2_U': .3334,
		'J3_S': .3314,
		'105_S': .3281,
		'97_U': .326,
		'22_P': .314,
		'87_U': .3233,
		'Q4_U': .3255,
		'J2_S': .3233,
		'65_S': .3221,
		'95_S': .3224,
		'104_S': .3222,
		'75_S': .321,
		'85_S': .3206,
		'J6_U': .3185,
		'Q3_U': .3163,
		'103_S': .3142,
		'106_U': .3116,
		'J5_U': .3126,
		'54_S': .3098,
		'102_S': .306,
		'Q2_U': .3072,
		'96_U': .3061,
		'64_S': .3042,
		'86_U': .3043,
		'76_U': .3041,
		'94_S': .3035,
		'74_S': .3021,
		'J4_U': .3035,
		'84_S': .3016,
		'93_S': .2978,
		'J3_U': .2944,
		'53_S': .2918,
		'105_U': .2921,
		'92_S': .2898,
		'65_U': .287,
		'63_S': .2855,
		'95_U': .2863,
		'J2_U': .2856,
		'75_U': .2854,
		'104_U': .2855,
		'43_S': .2828,
		'85_U': .2847,
		'73_S': .283,
		'83_S': .2828,
		'82_S': .2773,
		'103_U': .2768,
		'52_S': .273,
		'54_U': .2737,
		'62_S': .2665,
		'64_U': .2676,
		'102_U': .2679,
		'42_S': .2649,
		'72_S': .2644,
		'94_U': .2659,
		'74_U': .2651,
		'84_U': .2642,
		'93_U': .2597,
		'32_S': .2561,
		'53_U': .2546,
		'92_U': .251,
		'63_U': .2474,
		'43_U': .2449,
		'73_U': .2447,
		'83_U': .244,
		'82_U': .2379,
		'52_U': .2343,
		'62_U': .2269,
		'42_U': .2256,
		'72_U': .2244,
		'32_U': .2161
		}

twoPlayerHoleWinOdds = {
		'AA_P': .8493,
		'KK_P': .8212,
		'QQ_P': .7963,
		'JJ_P': .7715,
		'1010_P': .7466,
		'99_P': .7167,
		'88_P': .6872,
		'AK_S': .6622,
		'77_P': .6573,
		'AQ_S': .6531,
		'AJ_S': .644,
		'AK_U': .6447,
		'A10_S': .6349,
		'AQ_U': .6351,
		'AJ_U': .6254,
		'KQ_S': .6241,
		'66_P': .627,
		'A9_S': .6151,
		'A10_U': .6157,
		'KJ_S': .6148,
		'A8_S': .6051,
		'K10_S': .6059,
		'KQ_U': .6043,
		'A7_S': .5939,
		'A9_U': .5945,
		'KJ_U': .5944,
		'55_P': .5964,
		'QJ_S': .5907,
		'K9_S': .5864,
		'A5_S': .5806,
		'A6_S': .5818,
		'A8_U': .5837,
		'K10_U': .5849,
		'Q10_S': .5817,
		'A4_S': .5714,
		'A7_U': .5717,
		'K8_S': .5679,
		'A3_S': .5634,
		'QJ_U': .5691,
		'K9_U': .5641,
		'A5_U': .5574,
		'A6_U': .5587,
		'Q9_S': .5622,
		'K7_S': .5585,
		'J10_S': .5615,
		'A2_S': .5551,
		'Q10_U': .5595,
		'44_P': .5626,
		'A4_U': .5473,
		'K6_S': .548,
		'K8_U': .5443,
		'Q8_S': .5442,
		'A3_U': .5386,
		'K5_S': .5383,
		'J9_S': .5411,
		'Q9_U': .5386,
		'J10_U': .5383,
		'K7_U': .5342,
		'A2_U': .5295,
		'K4_S': .5289,
		'Q7_S': .5252,
		'K6_U': .523,
		'K3_S': .5207,
		'109_S': .5238,
		'J8_S': .5231,
		'33_P': .5284,
		'Q6_S': .6168,
		'Q8_U': .5193,
		'K5_U': .5125,
		'J9_U': .5164,
		'K2_S': .5124,
		'Q5_S': .5071,
		'108_S': .5051,
		'K4_U': .5023,
		'J7_S': .5045,
		'Q4_S': .4976,
		'Q7_U': .499,
		'109_U': .4982,
		'J8_U': .4971,
		'K3_U': .4933,
		'Q6_U': .49,
		'Q3_S': .4894,
		'98_S': .4886,
		'107_S': .4865,
		'J6_S': .4857,
		'K2_U': .4842,
		'22_P': .4939,
		'Q2_S': .481,
		'Q5_U': .4796,
		'J5_S': .4782,
		'108_U': .4782,
		'J7_U': .4773,
		'Q4_S': .4976,
		'Q7_U': .499,
		'109_U': .4982,
		'J8_U': .4971,
		'K3_U': .4933,
		'Q6_U': .49,
		'Q3_S': .4894,
		'98_S': .4886,
		'107_S': .4865,
		'J6_S': .4857,
		'K2_U': .4842,
		'22_P': .4939,
		'Q2_S': .481,
		'Q5_U': .4796,
		'J5_S': .4782,
		'108_U': .4782,
		'J7_U': .4773,
		'Q4_U': .4692,
		'97_S': .4699,
		'J4_S': .4687,
		'106_S': .468,
		'J3_S': .4604,
		'Q3_U': .4602,
		'98_U': .4607,
		'87_S': .4568,
		'107_U': .4583,
		'J6_U': .4571,
		'96_S': .4515,
		'J2_S': .452,
		'Q2_U': .4511,
		'105_S': .449,
		'104_S': .442,
		'97_U': .4407,
		'86_S': .4382,
		'J4_U': .4387,
		'106_U': .4385,
		'95_S': .4331,
		'103_S': .4338,
		'76_S': .4283,
		'J3_U': .4297,
		'87_U': .4269,
		'102_S': .4254,
		'85_S': .4199,
		'96_U': .421,
		'J2_U': .4205,
		'105_U': .4186,
		'94_S': .4141,
		'75_S': .4098,
		'104_U': .4106,
		'93_S': .4081,
		'86_U': .4070,
		'65_S': .4035,
		'84_S': .401,
		'95_U': .4014,
		'103_U': .4016,
		'92_S': .3997,
		'76_U': .3965,
		'74_S': .3911,
		'102_U': .3924,
		'54_S': .3853,
		'85_U': .3874,
		'64_S': .3848,
		'83_S': .3828,
		'94_U': .3809,
		'75_U': .3767,
		'82_S': .3768,
		'73_S': .3730,
		'93_U': .3743,
		'65_U': .3701,
		'53_S': .3676,
		'63_S': .3669,
		'84_U': .3571,
		'92_U': .3652,
		'43_S': .3573,
		'74_U': .3566,
		'72_S': .3544,
		'54_U': .3507,
		'64_U': .35,
		'52_S': .3493,
		'62_S': .3484,
		'83_U': .3475,
		'42_S': .3392,
		'82_U': .3409,
		'73_U': .3372,
		'53_U': .3316,
		'63_U': .3307,
		'32_S': .3309,
		'43_U': .3207,
		'72_U': .3171,
		'52_U': .3119,
		'62_U': .3108,
		'42_U': .3012,
		'32_U': .2924
		}
