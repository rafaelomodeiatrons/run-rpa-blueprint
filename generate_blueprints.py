import json
import copy

TEMPLATE_FILE = "blueprint_template.json"
OUTPUT_FILE = "blueprints_ENERGIA_copel_fluxo_completo_com_todos_os_indice_210.json"

REGISTROS = [
    {
        "cnpj": "61585865000151",
        "senha": "Raia2025*",
        "unidade_consumidora": "100059384",
    },
    {"cnpj": "61585865100962", "senha": "raia1234", "unidade_consumidora": "100141781"},
    {
        "cnpj": "61585865000151",
        "senha": "Raia2025*",
        "unidade_consumidora": "100212654",
    },
    {
        "cnpj": "61585865000151",
        "senha": "Raia2025*",
        "unidade_consumidora": "100550142",
    },
    {
        "cnpj": "61585865000151",
        "senha": "Raia2025*",
        "unidade_consumidora": "102326142",
    },
    {
        "cnpj": "61585865000151",
        "senha": "Raia2025*",
        "unidade_consumidora": "102961972",
    },
    {
        "cnpj": "61585865000151",
        "senha": "Raia2025*",
        "unidade_consumidora": "103551590",
    },
    {
        "cnpj": "61585865000151",
        "senha": "Raia2025*",
        "unidade_consumidora": "104031239",
    },
    {
        "cnpj": "61585865000151",
        "senha": "Raia2025*",
        "unidade_consumidora": "104144327",
    },
    {
        "cnpj": "61585865000151",
        "senha": "Raia2025*",
        "unidade_consumidora": "104426250",
    },
    {
        "cnpj": "61585865000151",
        "senha": "Raia2025*",
        "unidade_consumidora": "104488131",
    },
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "1045385"},
    {
        "cnpj": "61585865000151",
        "senha": "Raia2025*",
        "unidade_consumidora": "104956755",
    },
    {
        "cnpj": "61585865000151",
        "senha": "Raia2025*",
        "unidade_consumidora": "105222771",
    },
    {
        "cnpj": "61585865000151",
        "senha": "Raia2025*",
        "unidade_consumidora": "105351334",
    },
    {
        "cnpj": "61585865000151",
        "senha": "Raia2025*",
        "unidade_consumidora": "105456420",
    },
    {
        "cnpj": "61585865000151",
        "senha": "Raia2025*",
        "unidade_consumidora": "105713643",
    },
    {
        "cnpj": "61585865000151",
        "senha": "Raia2025*",
        "unidade_consumidora": "105792462",
    },
    {
        "cnpj": "61585865000151",
        "senha": "Raia2025*",
        "unidade_consumidora": "106174614",
    },
    {
        "cnpj": "61585865000151",
        "senha": "Raia2025*",
        "unidade_consumidora": "106174711",
    },
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "10622527"},
    {
        "cnpj": "61585865000151",
        "senha": "Raia2025*",
        "unidade_consumidora": "106312669",
    },
    {
        "cnpj": "61585865000151",
        "senha": "Raia2025*",
        "unidade_consumidora": "106426818",
    },
    {
        "cnpj": "61585865000151",
        "senha": "Raia2025*",
        "unidade_consumidora": "106454714",
    },
    {
        "cnpj": "61585865000151",
        "senha": "Raia2025*",
        "unidade_consumidora": "106652923",
    },
    {
        "cnpj": "61585865000151",
        "senha": "Raia2025*",
        "unidade_consumidora": "107157527",
    },
    {
        "cnpj": "61585865000151",
        "senha": "Raia2025*",
        "unidade_consumidora": "107783525",
    },
    {
        "cnpj": "61585865000151",
        "senha": "Raia2025*",
        "unidade_consumidora": "107924412",
    },
    {
        "cnpj": "61585865000151",
        "senha": "Raia2025*",
        "unidade_consumidora": "108799069",
    },
    {
        "cnpj": "61585865000151",
        "senha": "Raia2025*",
        "unidade_consumidora": "109375572",
    },
    {
        "cnpj": "61585865000151",
        "senha": "Raia2025*",
        "unidade_consumidora": "109375645",
    },
    {
        "cnpj": "61585865000151",
        "senha": "Raia2025*",
        "unidade_consumidora": "109375670",
    },
    {
        "cnpj": "61585865000151",
        "senha": "Raia2025*",
        "unidade_consumidora": "109456092",
    },
    {
        "cnpj": "61585865000151",
        "senha": "Raia2025*",
        "unidade_consumidora": "109981758",
    },
    {
        "cnpj": "61585865000151",
        "senha": "Raia2025*",
        "unidade_consumidora": "110028414",
    },
    {
        "cnpj": "61585865000151",
        "senha": "Raia2025*",
        "unidade_consumidora": "111507995",
    },
    {
        "cnpj": "61585865000151",
        "senha": "Raia2025*",
        "unidade_consumidora": "111586399",
    },
    {
        "cnpj": "61585865000151",
        "senha": "Raia2025*",
        "unidade_consumidora": "112032079",
    },
    {
        "cnpj": "61585865000151",
        "senha": "Raia2025*",
        "unidade_consumidora": "112299679",
    },
    {
        "cnpj": "61585865000151",
        "senha": "Raia2025*",
        "unidade_consumidora": "112529720",
    },
    {
        "cnpj": "61585865000151",
        "senha": "Raia2025*",
        "unidade_consumidora": "112874169",
    },
    {
        "cnpj": "61585865000151",
        "senha": "Raia2025*",
        "unidade_consumidora": "113681143",
    },
    {
        "cnpj": "61585865000151",
        "senha": "Raia2025*",
        "unidade_consumidora": "113843593",
    },
    {
        "cnpj": "61585865000151",
        "senha": "Raia2025*",
        "unidade_consumidora": "114075778",
    },
    {
        "cnpj": "61585865000151",
        "senha": "Raia2025*",
        "unidade_consumidora": "114614504",
    },
    {
        "cnpj": "61585865000151",
        "senha": "Raia2025*",
        "unidade_consumidora": "114706590",
    },
    {
        "cnpj": "61585865000151",
        "senha": "Raia2025*",
        "unidade_consumidora": "115159100",
    },
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "11553251"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "11589310"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "12513873"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "12630047"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "12808849"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "13703625"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "14510723"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "16004299"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "1708490"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "1728750"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "1840568"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "1895265"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "19370776"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "19866046"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "2025027"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "20638817"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "2067471"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "21215960"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "2540924"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "25679880"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "281140"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "29210739"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "29529646"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "29940516"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "3031071"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "32761201"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "34300384"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "34504290"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "34751718"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "35068515"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "35639148"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "36435392"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "36498068"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "37030620"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "3712761"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "3866874"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "40242749"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "4044185"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "4323424"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "43297056"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "43322425"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "4656490"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "46624066"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "47027517"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "484598"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "48672343"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "49047779"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "49825313"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "5013453"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "50444433"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "50902725"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "52396975"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "5247047"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "52745902"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "5382939"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "54185998"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "54266106"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "54421462"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "54518091"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "55872034"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "56750625"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "57513368"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "59475307"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "59651873"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "63491354"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "64020363"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "6609210"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "66548977"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "67161820"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "67317294"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "67514847"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "67515088"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "67563643"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "68602286"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "68759886"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "69069174"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "70119198"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "71170448"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "71424628"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "72516"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "7265492"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "72667273"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "72897627"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "74005871"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "74789678"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "7531397"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "75415704"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "75489473"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "75565676"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "75851334"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "76097617"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "76316491"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "77519701"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "7801149"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "78459281"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "79001866"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "79441653"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "79961568"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "80724159"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "80924948"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "81134142"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "81301324"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "81624328"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "8223327"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "82292590"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "83706259"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "84009705"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "84603879"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "85036994"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "85206148"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "85421600"},
    {"cnpj": "85429961", "senha": "Raia2025*", "unidade_consumidora": "85429961"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "86054686"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "86069560"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "86264753"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "86291300"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "86320610"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "86635352"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "87065606"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "87066475"},
    {"cnpj": "61585865322868", "senha": "#Raia2026", "unidade_consumidora": "87068338"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "87068656"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "87068834"},
    {"cnpj": "60605664011736", "senha": "#Raia2026", "unidade_consumidora": "87074958"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "87169525"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "87601150"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "87601800"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "88144496"},
    {"cnpj": "60605664036054", "senha": "raia1234", "unidade_consumidora": "88172961"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "88204510"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "88356167"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "88934969"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "89030362"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "89036913"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "89332555"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "89639383"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "89640527"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "89753070"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "90156978"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "90814169"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "90987039"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "91614341"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "91843073"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "91870631"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "91906130"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "92209319"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "92487190"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "9258361"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "92686540"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "93224397"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "94943834"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "9511032"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "95422048"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "95983040"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "97614793"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "98943189"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "99025574"},
    {"cnpj": "61585865000151", "senha": "Raia2025*", "unidade_consumidora": "99490684"},
]


def normalize_registro(registro):
    if isinstance(registro, dict):
        return {
            chave: "" if valor is None else str(valor)
            for chave, valor in registro.items()
        }

    return {"indice": "" if registro is None else str(registro)}


def ensure_variables_dict(blueprint):
    variables = blueprint.get("variables")

    if not isinstance(variables, list) or not variables:
        blueprint["variables"] = [{}]
        return blueprint["variables"][0]

    if not isinstance(variables[0], dict):
        blueprint["variables"][0] = {}

    return blueprint["variables"][0]


with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
    template = json.load(f)

blueprints = []
for registro in REGISTROS:
    bp = copy.deepcopy(template)
    variables = ensure_variables_dict(bp)
    variables.update(normalize_registro(registro))
    blueprints.append(bp)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(blueprints, f, ensure_ascii=False, indent=2)

print(f"OK -> {OUTPUT_FILE} gerado com {len(blueprints)} itens")
