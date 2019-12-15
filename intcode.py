class IntCode:
    def __init__(self, program, *args):
        self.memory = program.copy() + [0] * (4096 - len(program))
        self.inputs = [*args]
        self.pc = 0
        self.bp = 0
        self.halted = False
        self.output = []

    def run(self, *args):
        def param(offset):
            if self.memory[self.pc] // 10 ** (offset + 1) % 10 == 2:
                return self.memory[self.memory[self.pc + offset] + self.bp]
            elif self.memory[self.pc] // 10 ** (offset + 1) % 10 == 1:
                return self.memory[self.pc + offset]
            else:
                return self.memory[self.memory[self.pc + offset]]
        
        def store(offset, value):
            if self.memory[self.pc] // 10 ** (offset + 1) % 10 == 2:
                self.memory[self.memory[self.pc + offset] + self.bp] = int(value)
            else:
                self.memory[self.memory[self.pc + offset]] = int(value)

        self.inputs += [*args]
        
        while not self.halted:
            #print("DEBUG:", self.pc, program[self.pc])
            opcode = self.memory[self.pc] % 100
            if opcode == 1: # ADD(src1, src2, dest)
                store(3, param(1) + param(2))
                self.pc += 4

            elif opcode == 2: # MUL(src1, src2, dest)
                store(3, param(1) * param(2))
                self.pc += 4

            elif opcode == 3: # INPUT(dest)
                if self.inputs:
                    store(1, self.inputs.pop(0))
                    self.pc += 2
                else:
                    break

            elif opcode == 4: # OUTPUT(src)
                self.output.append(param(1))
                self.pc += 2

            elif opcode == 5: # JNZ(flag, loc)
                if param(1) != 0:
                    self.pc = param(2)
                else:
                    self.pc += 3

            elif opcode == 6: # JZ(flag, loc)
                if param(1) == 0:
                    self.pc = param(2)
                else:
                    self.pc += 3

            elif opcode == 7: # LT(src1, src2, dest)
                store(3, param(1) < param(2))
                self.pc += 4

            elif opcode == 8: # EQ(src1, src2, dest)
                store(3, param(1) == param(2))
                self.pc += 4

            elif opcode == 9: # BP(offset)
                self.bp += param(1)
                self.pc += 2

            elif opcode == 99: # HALT
                self.halted = True

            else:
                raise ValueError('Invalid opcode `' + str(opcode) + '` at instruction ' + str(self.pc))
        
        return self.output