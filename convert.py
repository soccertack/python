#!/usr/bin/python3

# Convert from this
#	/* VMPIDR_EL2 */
#	{ Op0(0b11), Op1(0b100), CRn(0b0000), CRm(0b0000), Op2(0b101),
#	  trap_el2_reg, reset_el2_val, VMPIDR_EL2, 0 },
#
# to this
# { SYS_DESC(SYS_VPIDR_EL2), trap_el2_reg, reset_el2_val, VPIDR_EL2, 0 },
# and this.
# #define SYS_VPIDR_EL2                   sys_reg(3, 4, 0, 0, 0)

import re

def convert(line):
	sp = re.split(r'\(|\)',line)
	#print (sp[1], sp[3], sp[5], sp[7], sp[9])
	return (int(sp[1], 2), int(sp[3], 2), int(sp[5], 2), int(sp[7], 2), int(sp[9], 2))

def get_reg_name(sp):
	#print(sp[2][:-1])
	return sp[2][:-1]

def print_desc(name):
	print("\t{ SYS_DESC(SYS_%s), trap_el2_reg, reset_el2_val, %s, 0 }," % (name, name))

def print_def(name, op0, op1, crn, crm, op2):
	print("#define SYS_%s\t\t\tsys_reg(%d, %d, %d, %d, %d)" % (name, op0, op1, crn, crm, op2))

with open("old.patch") as f:
	state = 0
	for line in f:
		line = line.strip()
		sp = line.split()

		if not len(sp):
			continue

		if sp[0] == "/*":
			continue
		if sp[0] == "{":
			#print (line)
			op0, op1, crn, crm, op2 = convert(line)
			continue
		if sp[0] == "trap_el2_reg,":
			name = get_reg_name(sp)
			#print_desc(name)
			print_def(name, op0, op1, crn, crm, op2)
			continue

		print ("err")
		print (line)
