import re
import string
import math
import copy

# define and save knowledge


class Predicate:
    def __init__(self):
        self.name = ''
        self.arguments = []

    def add_order_arguments(self, arguments):
        self.arguments.append(arguments)

    def parse(self, line):
        tempt = re.findall(r'\w+', line)
        self.name = tempt[0]
        tempt.remove(self.name)
        self.add_order_arguments(tempt)

    def get_name(self):
        return self.name

    def get_arguments(self):
        return self.arguments

    def print(self):
        print(self.name)
        print(self.arguments)


class PredicateLevel2(Predicate):
    def __init__(self):
        super().__init__()
        self.children = []          #cac predicate hop lai de suy dien ra vi tu no vd: p1^p2^...^pn => q thi children la
                                    #[p1, p2,.., pn]
        self.order = 0              #so cac menh de co the suy dien ra vi tu
        self.reference_variable = [] # vd: reference_variable[0] = [[Person,NiceNePhew],[Parent,NiceNePhes],[Person,Paren]]
                                    # luu theo ten luon ung voi tung list la tung predicate
                                     # co luu ca cac bien con cua cach suy dien khac suy dien khac (dau ';')

    def add_order_children(self, line, knowledge_base):
        line = line.split('),')
        list_of_children = []
        list_of_reference = [] #luu vi tri cac bien tuong ung voi cac predicate tu trai sang phai
        list_of_reference.append(self.arguments)
        for i in range(len(line) - 1):
            line[i] = line[i] + ')'
        for i in line:
            order_chaining = PredicateLevel2()
            order_chaining.parse_to_input(i, knowledge_base)
            for j in knowledge_base:
                if order_chaining.get_name() == j.get_name():
                    list_of_children.append(j)
                    list_of_reference.append(order_chaining.get_arguments())
                    break
        self.reference_variable.append(list_of_reference)
        self.children.append(list_of_children)
        self.order = self.order + 1

    def parse_to_input(self, line, base):
        if ':-' not in line:
            super().parse(line)
        else:
            main = line.split(':-')[0]
            children = line.split(':-')[1]
            super().parse(main)
            self.add_order_children(children, base)

    def get_order(self):
        return self.order

    def print_hardcore(self):
        super().print()
        for i in self.children:
            for j in i:
                print(j.get_name() + ' ')
            print('----')
        print(self.reference_variable)
        print(self.order)


def store_knowledge(lines):
    base = [] #list cac object predicate
    base.append(PredicateLevel2())
    for i in lines:
        flag = 0
        tempt = PredicateLevel2()
        tempt.parse_to_input(i, base)
        if ':-' not in i:
            for j in base:
                if j.get_name() == tempt.get_name():
                    order_children = re.findall(r'\w+', i)
                    order_children.remove(tempt.get_name())
                    j.add_order_arguments(order_children)
                    flag = 1
                    break
        else:
            for j in base:
                if j.get_name() == tempt.get_name():
                    j.add_order_children(i.split(':-')[1], base)
                    flag = 1
                    break
        if flag == 0:
            base.append(tempt)
    base.pop(0)
    return base



def read_question(line):
    ques = PredicateLevel2()
    ques.parse(line)
    return ques


# # backward-chaining


def is_variable(argument):
    if argument[0].isupper():
        return True
    return False


def unify_var(x, y, bind):
    if is_variable(x) and is_variable(y):
        if x in bind.keys():
            return False
        else:
            bind[x] = y
    elif not is_variable(x) and is_variable(y):
        return unify_var(y, x, bind)
    elif is_variable(x) and not is_variable(y):
        if x in bind.keys():
            if is_variable(bind[x]):
                bind[x] = y
            else:
                return False
    elif x != y:
        return False
    return bind


def unify(expr_x, expr_y):
    o = {}
    if len(expr_x) <= len(expr_y):
        for i in range(len(expr_x)):
            o = unify_var(expr_x[i], expr_y[i], o)
            if not o:
                return False
    else:
        unify(expr_x, expr_y)
    return o


def subst(o, predicate, order):
    for i in range(len(predicate.arguments[order])):
        if is_variable(predicate.arguments[order][i]):
            predicate.arguments[order][i] = o[predicate.arguments[order][i]]
    return predicate


def merge(o, o_tmp):
    if len(o) != len(o_tmp):
        return False
    check_len = 0
    for tmp_key in o_tmp.keys():
        for o_key in o.keys():
            if o[o_key] == tmp_key:
                o[o_key] = o_tmp[tmp_key]
                check_len = check_len + 1
    if check_len != len(o):
        return False


def combine_rest(ans, rest):
    if not ans or not rest:
        return False
    return ans + rest


def backward_chaining_ask(knowledge_base, goal, o):
    if goal.isempty():
        return o
    curr_goal = goal.pop(0)
    q_ = copy.deepcopy(subst(o, curr_goal))
    args = q_.arguments[0]
    curr_args = []
    for i in knowledge_base:
        if i.get_name() == curr_goal.get_name():
            curr_args = i.arguments[0]
    q = unify(curr_args, q_.arguments[0])
    o = merge(o, q)
    ans = []
    ans = combine_rest(ans, backward_chaining_ask(knowledge_base, goal, o))
    for i in curr_goal.children:
        goal.insert(0, i)
        ans_res = backward_chaining_ask(knowledge_base, goal, o)
        if not ans_res:
            ans_res = ans_res + ans


if __name__ == "__main__":
    with open('royal.txt', 'r') as f:
        press_F = f.read().split('.\n')
    tri_thuc = store_knowledge(press_F)
    question = input('?-')
    ques = PredicateLevel2()
    ques.parse_to_input(question)
    dich = []
    dich.append(ques)
    the_ta = {}
    ket_qua = []
    ket_qua = backward_chaining_ask(tri_thuc, dich, the_ta)
    print(ket_qua)




