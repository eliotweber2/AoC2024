function calcNext(program) {
    operand = program.iSet[program.ip+1]
    switch (program.iSet[program.ip]) {
      case 0: program.rA = parseInt(program.rA / 2**getCombo(operand,program)); program.ip += 2; break
      case 1: program.rB = program.rB ^ operand; program.ip += 2; break
      case 2: program.rB = getCombo(operand,program) % 8; program.ip += 2; break
      case 3: program.ip = program.rA == 0? program.ip + 2 : 0; break
      case 4: program.rB = program.rB ^ program.rC; program.ip += 2; break
      case 5: program.out += (',' + (getCombo(operand,program) % 8)); program.ip += 2; break
      case 6: program.rB = parseInt(program.rA / 2**getCombo(operand,program)); program.ip += 2; break
      case 7: program.rC = parseInt(program.rA / 2**getCombo(operand,program)); program.ip += 2; break
    }
  }
  
  function getCombo(op,program) {
    switch (op) {
      case 0: return 0
      case 1: return 1
      case 2: return 2
      case 3: return 3
      case 4: return program.rA
      case 5: return program.rB
      case 6: return program.rC
    }
  }
  
  program = {
    ip:0,
    rA:100,
    rB:0,
    rC:0,
    iSet: [0,3,5,4,3,0],
    out: '',
  }
  
  while (program.ip < program.iSet.length) {
    calcNext(program);
  }
  console.log(program)
  console.log(program.out.slice(1))
  
  