#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： 11360
# datetime： 2022/1/21 17:05 

import itertools

#
# def get_num_lst(li):
#     return list(itertools.permutations(li))


def get_num_lst(li):
    """
    number combination: num = len(li)!
    """
    res = []
    # lst[0]: sub node option
    # lst[1]: current combination
    stack = [[list(li).copy(), []]]
    while stack:
        lst = stack.pop()
        if not lst[0]:
            res.append(lst[1])
        else:
            for i, opt in enumerate(lst[0]):
                sub_node_opt = lst[0].copy()
                val = sub_node_opt.pop(i)
                combination = lst[1].copy()
                combination.append(val)
                stack.append([sub_node_opt, combination])
    print("input permutation num:", len(res))
    return res


def get_operation_lst(operator_lst, num=3):
    """
    operator combination: num = 4^num
    """

    res = []
    stack = [[i] for i in operator_lst]
    while stack:
        lst = stack.pop()
        if len(lst) == num:
            res.append(lst)
        else:
            for opt in operator_lst:
                _ = lst.copy()
                _.append(opt)
                stack.append(_)
    print("operator combination num:", len(res))
    return res


def twenty_four_pts(*args):
    """
    judge whether can take 24
    """
    lst = args
    operator = ["+", "-", "*", "/"]
    operator_lst = get_operation_lst(operator, num=len(lst)-1)
    permutation_lst = get_num_lst(lst)
    for num_opt in permutation_lst:
        num_opt = list(num_opt)
        for op_option in operator_lst:
            op_option_cpy = op_option.copy()
            num_option_cpy = num_opt.copy()
            success_flag = True
            res_stack = list()
            res_stack.append(num_option_cpy.pop(0))
            res_stack.append(num_option_cpy.pop(0))
            while op_option_cpy:
                op = op_option_cpy.pop(0)

                left = res_stack.pop(0)
                right = res_stack.pop(0)
                if op == "+":
                    res_stack.append(left + right)
                elif op == "-":
                    res_stack.append(left - right)
                elif op == "*":
                    res_stack.append(left * right)
                elif op == "/":
                    try:
                        res_stack.append(left / right)
                    except Exception as e:
                        print("[error] ", e)
                        success_flag = False
                        break
                else:
                    raise ValueError("[Error] Operator not in (+, -, *, /)")
                if num_option_cpy:
                    res_stack.append(num_option_cpy.pop(0))
            if not success_flag:
                continue
            if abs(res_stack[0] - 24) < 0.1:
                return num_opt, op_option
    raise ValueError("[Error] no result")


def is_opt_priority(obj_opt, ref_opt):
    """
    judge obj_opt and ref_opt priority
    """
    if obj_opt in ["*", "/"] and ref_opt in ["+", "-"]:
        return True
    else:
        return False


def parse(num_opt, op_opt):
    """
    parse to a Arithmetic expression
    """
    res_str = str(num_opt[0])
    for i in range(0, len(op_opt)):
        opt = op_opt[i]
        num = num_opt[i + 1]
        if i != len(op_opt) - 1:
            nxt_opt = op_opt[i + 1]
            if is_opt_priority(nxt_opt, opt):
                # 若下一个操作的优先级比当下高，则要加括号
                res_str = "(" + res_str + opt + str(num) + ")"
            else:
                res_str = res_str + opt + str(num)
        else:
            res_str = res_str + opt + str(num)
    return res_str + " = 24"


if __name__ == "__main__":
    try:
        num_option, operator_option = twenty_four_pts(10, 5, 11, 3)
        # num_option, operator_option = twenty_four_pts(10, 2, 1, 2, 3)

        print(num_option, operator_option)
        print(parse(num_option, operator_option))
    except Exception as e:
        print(e)
