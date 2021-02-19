import openpyxl

file_path = input(r'定义书路径').strip()
root_path = input(r'请输入要保存的文件路径').strip()
code_file = "simple_localizations.dart"

# excel book
wb = openpyxl.load_workbook(file_path,data_only=True)

# excel sheet
ws = wb["Sheet1"]

zh = ""
ja = ""
en = ""

get_text = ""

def creatMethonName(key):
    index = 0
    name = ""
    key_list = key.split("_")
    for st in key_list:
        if index != 0:
            st = st.capitalize()
        name = name + st
        index = index + 1
    return name

def creatList(list_value):
    string_list = list_value.split(",")
    string_value = ""
    index = 0
    for st in string_list:
        if len(string_list)-1 == index:
            string_value = string_value + "'" + st + "'"
        else:
            string_value = string_value + "'" + st + "'" + ","
        index = index + 1
    return string_value


for row in ws.iter_rows(min_row=2):
    if(row[4].value == "String"):
        get_text = get_text + "String get " + f"{creatMethonName(row[0].value)}" + "{\n" \
            "return " + "_stringMap['" + f"{row[0].value}"+"'];\n" \
            "}\n"
        zh = zh + "'" + row[0].value +"'" + ":" + "'" + row[1].value + "'" + ",\n"
        ja = ja + "'" + row[0].value +"'" + ":" + "'" + row[2].value + "'" + ",\n"
        en = en + "'" + row[0].value +"'" + ":" + "'" + row[3].value + "'" + ",\n"

    if(row[4].value == "List"):
        get_text = get_text + "List<String> get " + f"{creatMethonName(row[0].value)}" + "{\n" \
            "return " + "_stringMap['" + f"{row[0].value}"+"'] as List<String>;\n" \
            "}\n"
        zh = zh + "'" + row[0].value +"'" + ":" + "[" + creatList(row[1].value) + "]" + ",\n"
        ja = ja + "'" + row[0].value +"'" + ":" + "[" + creatList(row[2].value) + "]" + ",\n"
        en = en + "'" + row[0].value +"'" + ":" + "[" + creatList(row[3].value) + "]" + ",\n"





contentCode = "import 'dart:ui';\n" \
    "import 'package:flutter/cupertino.dart';\n" \
    "class SimpleLocalizations{\n" \
    "final Locale locale;\n" \
    "SimpleLocalizations(this.locale);\n" \
    "static SimpleLocalizations of(BuildContext context){\n" \
    "return Localizations.of<SimpleLocalizations>(context, SimpleLocalizations);\n" \
    "}\n" \
    "static Map<String,Map<String,dynamic>> _localizedValues ={\n" \
    "'zh':{\n" \
    f"{zh}\n" \
    "},\n" \
    "'ja':{\n" \
    f"{ja}\n" \
    "},\n" \
    "'en':{\n" \
    f"{en}\n" \
    "},\n" \
    "};\n" \
    "Map<String,dynamic> get _stringMap{\n" \
    "return _localizedValues[locale.languageCode];\n" \
    "}\n" \
    f"{get_text}" \
    "}"


f = open(root_path+"/"+code_file, 'w', encoding='UTF-8')
f.write(contentCode)
f.close()