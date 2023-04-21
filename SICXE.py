# generate optable
OPTAB = {}
fIns = open('instrution.txt', 'r')
lIns = fIns.readlines()
for ins in lIns:
    tmp = ins.split()
    OPTAB[tmp[0]] = tmp[1:]
# print(OPTAB)
fIns.close()
# generate registers
REGS = {}
fReg = open('register.txt', 'r')
lRegs = fReg.readlines()
for reg in lRegs:
    tmp = reg.split()
    REGS[tmp[0]] = tmp[1]
# print(REGS)
fReg.close()
# pass1
code = []
f1 = open('input_SICXE.txt', 'r')
lines = f1.readlines()
for line in lines:
    tmp = line.split()
    # print(len(tmp))
    if len(tmp) == 2:
        tmp.insert(0, None)
    elif len(tmp) == 1:
        tmp.append(None)
        tmp.insert(0, None)
    code.append(tmp)
# for i in code:
#     print(i)
SYMTAB = {}
count = 0
LOCCTR = 0
ws = ""
fSymbol = open('pass1.txt', 'w')
for i in range(len(code)):
    count = i + 1
    if code[i][1] == "START":
        START = int(code[i][2])
        # SYMTAB[code[i][0]] = str(START)
        LOCCTR = START
        fSymbol.write(hex(LOCCTR)[2:].upper().zfill(4) + '\t')
        for j in range(len(code[i])):
            if code[i][j] != None:
                ws += (code[i][j] + '\t')
            # print(ws)
        ws += '\n'
        fSymbol.write(ws)
        break
    else:
        LOCCTR = 0

while code[count][1] != "END":
    # search symbol table
    if code[count][1] != "BASE":
        if code[count][0] != None:
            fSymbol.write(hex(LOCCTR)[2:].upper().zfill(4) + '\t')
        else:
            fSymbol.write(hex(LOCCTR)[2:].upper().zfill(4) + '\t' + '\t' + '\t')
    else:
        fSymbol.write('\t' + '\t')
    ws = ""
    for j in range(len(code[count])):
        if code[count][j] != None:
            ws += (code[count][j] + '\t')
        # print(ws)
    ws += '\n'
    fSymbol.write(ws)
    if code[count][0] not in SYMTAB and code[count][0] != None:
        # SYMTAB[code[count][0]] = str(LOCCTR).encode('utf-8').hex()
        SYMTAB[code[count][0]] = hex(LOCCTR)[2:].upper()
    elif code[count][0] in SYMTAB:
        print("error: duplicate symbol")
    # search optable
    if code[count][1] in OPTAB:
        LOCCTR += int(OPTAB[code[count][1]][0])
    elif code[count][1] == "WORD":
        LOCCTR += 3
    elif code[count][1] == "RESW":
        LOCCTR += 3 * int(code[count][2])
    elif code[count][1] == "RESB":
        LOCCTR += int(code[count][2])
    elif code[count][1] == "BYTE":
        # print("BYTE",int(code[count][2][2:len(code[count][2])-1].encode('utf-8').hex(),16))
        if code[count][2][0] == 'C':
            LOCCTR += len(code[count][2][2:len(code[count][2]) - 1])
            # print("L", hex(LOCCTR))
        elif code[count][2][0] == 'X':
            LOCCTR += 1
    elif code[count][1][0] == "+":
        LOCCTR += 4
        # format4
    # else:
    #     print("error: unknown opcode")

    count += 1
programLength = hex(LOCCTR - START)[2:].upper()
fSymbol.write('\t' + '\t')
ws = ""
for j in range(len(code[count])):
    if code[count][j] != None:
        ws += (code[count][j] + '\t')
    # print(ws)
ws += '\n'
fSymbol.write(ws)
# print("length",programLength)

fSymbol.close()
print(SYMTAB)

# # pass2
#
# def format2(ins,reg):
#     print("format2",ins,reg)
#     objcode = list(OPTAB[ins][1])
#
#     if len(reg)>1:
#         r1 = REGS[reg[0]]
#         r2 = REGS[reg[2]]
#     else:
#         r1 = REGS[reg]
#         r2 = '0'
#     objcode.append(r1)
#     objcode.append(r2)
#     print(objcode)
#     return "".join(objcode)
#
# nixbpe = [0]*6
# disp = 0
# print(nixbpe)
# def format3(ins,label,pc,base,TA):
#     # print("format3",ins)
#     if label[0] == '#':
#         nixbpe[1] = 1;
#         nixbpe[0] = 0;
#         TA = int(SYMTAB[label]) - pc
#         if TA >= -2048 and TA <= 2047:
#             if TA < 0:
#                 TA = twosComp(TA, 2) & int("0000111111111111", 2)
#             obj = int(OPCODETAB[self.op][1], 16)
#             obj = obj << 4
#             obj += flagConstructor(0, 1, 0, 0, 1, 0)
#             obj = obj << 12
#             obj += TA
#             # Base Relative
#             else:
#                 TA = self.SYMTAB[self.arg1] - self.BASE
#                 if TA >= 0 and TA <= 4095:
#                     obj = int(OPCODETAB[self.op][1], 16)
#                     obj = obj << 4
#                     obj += flagConstructor(0, 1, 0, 1, 0, 0)
#                     obj = obj << 12
#                     obj += TA
#     elif label[0] == '@':
#             if TA >= -2048 and TA <= 2047:
#                                 if TA < 0:
#                                     TA = twosComp(TA, 2) & int("0000111111111111", 2)
#                                 obj = int(OPCODETAB[self.op][1], 16)
#                                 obj = obj << 4
#                                 obj += flagConstructor(0, 1, 0, 0, 1, 0)
#                                 obj = obj << 12
#                                 obj += TA
#                             # Base Relative
#                             else:
#                                 TA = self.SYMTAB[self.arg1] - self.BASE
#                                 if TA >= 0 and TA <= 4095:
#                                     obj = int(OPCODETAB[self.op][1], 16)
#                                     obj = obj << 4
#                                     obj += flagConstructor(0, 1, 0, 1, 0, 0)
#                                     obj = obj << 12
#                                     obj += TA
#                                 else:
#         nixbpe[1] = 0;
#         nixbpe[0] = 1;
#     else:
#
#     return 0
#
#
# def format4(ins,label,TA):
#     disp = 0
#     if label[0] == '#':
#         if label in SYMTAB.keys():
#             TA = SYMTAB[label]
#             # PC Relative
#             disp = int(OPTAB[ins][1], 16)
#             disp = disp << 4
#             for i in range(len(nixbpe)):
#                 disp += nixbpe[i]<<(len(nixbpe)-1)
#             disp = disp << 20
#             disp += TA
#         # Immediate
#         else:
#             TA = SYMTAB[label]
#             disp = int(OPTAB[ins.op][1], 16)
#             disp = disp << 4
#             for i in range(len(nixbpe)):
#                 disp += nixbpe[i] << (len(nixbpe) - 1)
#             disp = disp << 20
#             disp += TA
#     elif label[0] = @:
#         TA = self.SYMTAB[self.arg1]
#         # PC Relative
#         obj = int(OPCODETAB[self.op][1], 16)
#         obj = obj << 4
#         obj += flagConstructor(1, 0, 0, 0, 0, 1)
#         obj = obj << 20
#         obj += TA
#     else:
#         TA = self.SYMTAB[self.arg1]
#         # PC Relative
#         obj = int(OPCODETAB[self.op][1], 16)
#         obj = obj << 4
#         obj += flagConstructor(1, 1, self.indexed, 0, 0, 1)
#         obj = obj << 20
#         obj += TA
#     return 0
#
#
# code2 = []
# fPass1 = open('pass1.txt', 'r')
# lines = fPass1.readlines()
# for line in lines:
#     tmp = line.split()
#     # print(len(tmp))
#     if len(tmp) == 3:
#         tmp.insert(1, None)
#     elif len(tmp) == 2:
#         if "BASE" in tmp or "END" in tmp:
#             tmp.insert(0, None)
#             tmp.insert(0, None)
#         else:
#             tmp.append(None)
#             tmp.insert(1, None)
#     # code2.append(tmp)
# print(code2)
# fRecord = open('pass2.txt', 'w')
# fRecord.write('H')
# count = 0
# BASE = 0
# PC = 0
# TA = ""
# for i in range(len(code2)):
#     count = i + 1
#     if code2[i][2] == "START":
#         fRecord.write(code2[i][1] + " " * (6 - len(code2[i][1])))
#         fRecord.write(code2[i][0].zfill(6).upper())
#         fRecord.write(programLength.zfill(6))
#         fRecord.write('\n')
#         break
#
# while code2[count][2] != "END":
#     operandAddress = 0
#     pc = code[count+1][0]
#
#     print("pc",pc)
#     # print(code2[count][2])
#     # if count%5 == 1:
#     #     fRecord.write('T'+'\n')
#     if code2[count][2] in OPTAB:
#         if code2[count][3] in SYMTAB:
#             oprandAddress = int(SYMTAB[code2[count][3]], 16)
#         else:
#             oprandAddress = 0
#             # set error flag?
#     else:
#         operandAddress = 0
#     if code2[count][2] in OPTAB :
#         if OPTAB[code2[count][2]][0] == '3':
#             if code2[count][2][0] == '+':
#                 format4(code2[count][2],code2[count][3])
#             else:
#                 format3(code2[count][3],code2[count][3])
#
#         elif OPTAB[code2[count][2]][0] == '2':
#             TA = format2(code2[count][2],code2[count][3])
#             print(TA)
#
#     count += 1
# fRecord.close()



