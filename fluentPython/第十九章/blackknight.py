#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

class BlackKnight:
    '''
    >>> from blackknight import BlackKnight
    >>> knight = BlackKnight()
    >>> knight.member
    next member is:
    'an arm'
    >>> del knight.member
    BLACK KNIGHT (loses an arm)
    -- 'Tis but a scrath.'
    >>> del knight.member
    BLACK KNIGHT (loses another arm)
    -- It's just a flesh wound.
    >>> del knight.member
    BLACK KNIGHT (loses a leg)
    -- I'm invincible!
    >>> del knight.member
    BLACK KNIGHT (loses another leg)
    -- All right, we'll call it a draw.
    '''

    def __init__(self):
        self.members = ['an arm', 'another arm', 'a leg', 'another leg']
        self.phrases = ["'Tis but a scrath.'",
                        "It's just a flesh wound.",
                        "I'm invincible!" ,
                        "All right, we'll call it a draw."
                        ]

    @property
    def member(self):
        print('next member is:')
        return self.members[0]

    @member.deleter
    def member(self):
        text = 'BLACK KNIGHT (loses {})\n -- {}'
        print(text.format(self.members.pop(0), self.phrases.pop(0)))