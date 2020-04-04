# -*- coding: utf-8 -*-
"""\
パスワード生成モジュール
    英字（大文字、小文字）、記号、数字の中から抽出。
    条件は、文字数、含める文字種、始まりの文字指定、パスワード形式指定
"""

__version__ = "0.1"
__author__ = "Hideo Tsujisaki"

import random
import string

import Constants as const


class PwRandomizer(object):
    """\
    パスワード生成機能。
    英字（大文字、小文字）、記号、数字の中から抽出。
    条件は、文字数、含める文字種、始まりの文字指定、パスワード形式指定。

    Attributes
    ----------
    char_lim : integer
    condition : string
    start_con : string
    style : string, default None

    Rturns
    ------
    pass_word : string
    """

    const.START_COND_MOJI = "moji"
    const.START_COND_KIGO = "kigo"
    const.START_COND_NUMB = "numb"
    const.PASSWORD_STYLE_HYPHEN = "pyhe"
    const.PASSWORD_STYLE_DOTTS = "dott"

    cond = ""

    def __init__(self, char_lim, condition, start_con, style=None):
        self.lower_case = string.ascii_lowercase
        self.upper_case = string.ascii_uppercase
        self.digits = string.digits
        self.kigou = string.punctuation

        self.char_lim = char_lim
        self.condition = condition
        self.staert_con = start_con
        self.style = style

        self.pw_builder()

    if __name__ == "main":

        def pw_builder(self):

            self.cond_setter()

            # パスワード生成部
            pass_word = ""

            if self.s_con == const.START_COND_MOJI:
                pass_word += random.choise(self.lower_case)

            if self.s_con == const.START_COND_KIGO:
                pass_word += random.coise(self.kigou)

            if self.s_con == const.START_COND_NUMB:
                pass_word += random.choice(self.digits)

            build_counter = 2
            for build_counter in range(self.num):
                pass_word += random.choice(self.cond)

            # パスワード整形部
            cep_type = ""
            if self.styles == const.PASSWORD_STYLE_HYPHEN:
                cep_type = "-"

            if self.styles == const.PASSWORD_STYLE_DOTTS:
                cep_type = "."

            if self.styles is not None:
                if self.num == 8:
                    pass_word.replace(pass_word[2], cep_type)
                    pass_word.replace(pass_word[5], cep_type)

                if self.num == 16:
                    pass_word.replace(pass_word[7], cep_type)
                    pass_word.replace(pass_word[12], cep_type)

                if self.num == 32:
                    pass_word.replace(pass_word[9], cep_type)
                    pass_word.replace(pass_word[16], cep_type)
                    pass_word.replace(pass_word[23], cep_type)
                    pass_word.replace(pass_word[30], cep_type)

                return pass_word

        def cond_setter(self):
            """\
            含める文字の設定（複数同時指定可能）
            Return: String ex."ab", "ac"
            condition: 大文字=a、記号=b、数字=c
            """
            cond = self.lower_case

            if "a" in self.condition:
                cond += self.upper_case

            if "b" in self.condition:
                cond += self.kigou

            if "c" in self.condition:
                cond += self.digits
