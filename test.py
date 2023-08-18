from sklearn import preprocessing
import numpy as np



def derivative(x):
    return x * (1.0 - x)


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))



# если результат больше 0.5 - спам, если меньше - нет
weight0 = [[0.40423460894175345, -4.079339863497263, 0.6967292203484402, -0.015425455091310984],
[-7.487008778942599, -10.302259286417454, 10.409832839251319, -2.2020266467091876],
[1.6534155123588483, 1.4784773857412215, 2.856400162252348, 6.261368123741618],
[-3.169245453157111, 22.303809215233553, -10.56154165497029, 7.766688979485359],
[-2.1180406391046835, 5.569343310265342, -22.87772946934069, -3.5711969045136676],
[20.46824555061894, 6.43673275607533, 9.80871272478868, 11.78138860906714],
[12.857777183568679, 27.57070383122827, -29.174091795483566, -11.884212127689931],
[0.3976394854243423, 12.894115214672759, -10.761609902812909, 0.08801721689946554],
[16.04297319468725, 17.434705458320042, -3.213272414712434, 8.066315504555888],
[7.600757381423674, -3.633390784392611, -14.60690460275852, 5.247489343748327],
[27.2403567617108, 22.12902085445737, -8.871590428793725, 6.173171545119145],
[-11.683163770308264, -3.1006085688514555, 17.232432264436802, 12.295622471417037],
[-1.4444018697946228, 7.1188906010422235, 7.219071139767233, 11.826360197584638],
[-2.820019126389712, -3.8643291543374736, -4.748658927288123, -11.486667537127916],
[4.6821078237060725, 6.617896743046495, -17.923493626744364, 6.446398397940678],
[0.8344415013485612, 30.606589543126624, -26.228757048853986, 1.8133698751045741],
[-9.904615013495954, 20.139657544957803, 6.887233499401572, 2.375890861385617],
[10.270965607288954, 2.1037427344990416, -10.932542972740885, -7.315759202266072],
[8.616520987000662, 8.081960348589755, -2.7161562238988464, -4.854952289368284],
[14.432531812705015, 9.317881075948316, -25.79324632365818, 5.719571716504207],
[17.537658884201324, 4.611554000474904, -23.518875291246292, 0.36141076775463726],
[-0.41052086650988967, 16.19963040732871, -6.2643456499306875, 13.002902745056602],
[6.368996274712632, 28.207332495758216, -71.8736040813807, 8.758840005021206],
[-1.4998418335016686, 3.1481831496929695, -18.990144854399453, -5.3834065896525285],
[16.85965382954473, -53.44711550192895, 35.76704443931404, 7.505232641554146],
[-0.38217165092469435, 3.2776443766657977, 37.413538314369326, 0.6013551051084516],
[11.357860708239565, -17.1512195746259, 44.5979340176899, 17.151398449146974],
[18.283850954506434, -4.569538145975427, -24.147844786761883, -5.900425547576235],
[14.011867558224598, -8.392292120167847, 4.6417344782770655, 9.94457525245897],
[2.802667269113863, -0.030011490681091588, 0.8575478177505635, -5.171019796251454],
[-2.5672008842586855, -18.152096653029542, 1.429003660356165, -2.9771941558588457],
[12.966704510212091, 17.712705909684548, 9.92809070586379, 9.677027967224694],
[-6.620653340064944, -1.1944654599237976, 3.1626220273022656, 15.007350909615994],
[6.681892343194486, -3.6318891820163683, 12.969766358555338, -1.9000358766523417],
[8.583645795210597, -10.976216637036842, 26.138659816093007, 8.220231734473252],
[6.670064595170486, 0.5343380368990268, -16.825656446975493, -3.6319742252049703],
[-10.134773824795838, -23.627266026300127, 16.314637553506635, 10.83287504141548],
[5.248836111655701, -0.7823932684500094, -9.427591983757436, 16.755288739909],
[0.1614160080429224, -13.361599331495697, 5.806830665846045, 12.249585709986553],
[5.221839591253508, -7.690354773929649, -12.458870451003909, 10.388105870420437],
[-2.0229224024029797, -0.4030014292675951, 19.60903484315859, 12.830506715035092],
[-6.12405056605261, -17.936533473014393, 16.329799518990143, 8.94861852116459],
[8.315032283092373, 10.31133553145075, 13.947694783423506, 15.528015383936735],
[4.814247955594636, -10.643976863142871, 22.8106710014111, 10.90945705027642],
[13.201199208268745, -0.17431605521228422, 29.08245780123027, 5.450910900659262],
[5.822564939608509, -41.92450795196759, 37.427779619727715, -5.838051996814376],
[-2.1669599710739305, 8.054255760482889, 4.859937911469122, 8.89300844246889],
[5.090996297200415, -20.56990813596579, -1.0805069070623858, -6.4732383603170955],
[1.5978925610647896, 17.348776284516703, 11.773668638491424, 4.856494913065862],
[-4.234616732340827, 2.38573623906879, 15.106089751357324, 19.193027778234818],
[14.59589723606852, 4.794144209722586, 5.304317693850646, 9.909292504713598],
[-4.219431574622243, 22.83790108629826, -32.783580126668575, -1.5202279243651273],
[11.613712312557613, 63.3081179985714, -37.46640800753089, 7.550795026269663],
[-3.7726231550287435, -0.14822201446214175, -7.177312009962561, 3.343319674853685],
[-12.6351887595828, 18.320848495419227, -8.55198991507869, -16.458276322793704],
[-10.873825933839655, 22.573411519669605, -10.116598171120451, 6.516086726403468],
[-3.8267027643897564, 10.8133774131014, -22.888646353285555, 12.71212085767578]]

weight1 = [[-18.81540906], [ 50.58816872], [-40.07230296], [-21.25255064]]

X =[]


data = open('spambase_new.data', "r")
data = data.read().split('\n')[:-1]
for line in data:
    curr = line.split(',')
    new_curr = []
    for item in curr:
        new_curr.append(float(item))
    X.append(new_curr)
    # print(new_curr, [float(curr[-1])])

# print(len(X), len(Y))
X = np.array(X)
X = preprocessing.scale(X)

layer_1 = sigmoid(np.dot(X, weight0))
# print(layer_1)
layer_2 = sigmoid(np.dot(layer_1,weight1))

for i in range(len(layer_2)):
    if layer_2[i][0] > 0.5:
        layer_2[i][0] = 1
        print('spam')
    else:
        layer_2[i][0] = 0
        print('not spam')

