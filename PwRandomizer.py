# -*- coding: utf-8 -*-
"""\
パスワード生成モジュール
    英字（大文字、小文字）、記号、数字の中から抽出。
    条件は、文字数、含める文字種、始まりの文字指定、パスワード形式指定
"""

__version__ = "0.1"
__author__  = "Hideo Tsujisaki"

from random import choice
from string import ascii_lowercase as strAscLow
from string import ascii_uppercase as strAscUpp
from string import digits as strDigi
from string import punctuation as strPunc

import constants as const


class PwBuildCenter(object):
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
    const.PASSWORD_STYLE_HYPHEN = "hype"
    const.PASSWORD_STYLE_DOTTS = "dott"


    def __init__(self, char_lim, condition, start_con, style):
        self.lower_case = strAscLow
        self.upper_case = strAscUpp
        self.digits = strDigi
        self.kigou = strPunc

        self.char_lim = char_lim
        self.condition = condition
        self.start_con = start_con
        self.style = style

        self.cond = ""
        self.pass_word =""


    def pw_builder(self):

        self.cond_setter()

        # パスワード生成部
        # 初めの文字の指定がある場合の設定（初期値は文字始まり）
        if self.start_con == const.START_COND_MOJI:
            self.pass_word += choice(self.lower_case)

        if self.start_con == const.START_COND_KIGO:
            self.pass_word += choice(self.kigou)

        if self.start_con == const.START_COND_NUMB:
            self.pass_word += choice(self.digits)

        # 残りの文字を2文字目から生成していく
        buildStart = 2
        buildEnd = self.char_lim + 1
        for ite in range(buildStart, buildEnd):
            self.pass_word += choice(self.cond)

        # パスワード整形部
        cep_type = ""
        if self.style == const.PASSWORD_STYLE_HYPHEN:
            cep_type = "-"

        if self.style == const.PASSWORD_STYLE_DOTTS:
            cep_type = "."

        if self.style is not None:
            restrucutPw = ""
            if self.char_lim == 8:
                restrucutPw += self.pass_word[0:2] + cep_type
                restrucutPw += self.pass_word[3:5] + cep_type
                restrucutPw += self.pass_word[6:]
                self.pass_word = restrucutPw

            if self.char_lim == 16:
                restrucutPw += self.pass_word[0:5] + cep_type
                restrucutPw += self.pass_word[6:10] + cep_type
                restrucutPw += self.pass_word[11:]
                self.pass_word = restrucutPw

            if self.char_lim == 24:
                restrucutPw += self.pass_word[0:4] + cep_type
                restrucutPw += self.pass_word[5:9] + cep_type
                restrucutPw += self.pass_word[10:14] + cep_type
                restrucutPw += self.pass_word[15:19] + cep_type
                restrucutPw += self.pass_word[20:]
                self.pass_word = restrucutPw

        return self.pass_word

    def cond_setter(self):
        """\
            含める文字の設定（複数同時指定可能）
            Return: String ex."ab", "ac"
            condition: 大文字=A、記号=B、数字=C
            """
        self.cond = self.lower_case

        if "A" in self.condition:
            self.cond += self.upper_case

        if "B" in self.condition:
            self.cond += self.kigou

        if "C" in self.condition:
            self.cond += self.digits
