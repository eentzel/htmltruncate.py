#!/usr/bin/python

# Copyright (c) 2015 Eric Entzel

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import htmltruncate
import unittest

class TruncateTest(unittest.TestCase):
    cases = ( ('this <b>word</b> is bolded', 4, "this"),
              ('this <b>word</b> is bolded', 6, "this <b>w</b>"),
              ('this <b>word</b> is bolded', 8, "this <b>wor</b>"),
              ('this <b>word</b> is bolded', 10, "this <b>word</b> "),
              ('this <b>word</b> is bolded', 700, "this <b>word</b> is bolded"),
              ('the second tag <span class="hello">is closed, but is the <a href="/test.html">first one</a> closed too?</span>', 52,
               'the second tag <span class="hello">is closed, but is the <a href="/test.html">first one</a> close</span>'),
              ("This is a test of the truncating feature in EDCZ&trade; please use with caution.", 65,
               "This is a test of the truncating feature in EDCZ&trade; please use with"),
              ("<p>Well here's another test of truncation <span>with</span> a little bit o markup and a bunch more stuff</p>", 65,
               "<p>Well here's another test of truncation <span>with</span> a little bit o markup</p>"),
              ("This is a test of the truncating feature in EDCZ&trade; please <span>use</span> with caution.", 65,
               "This is a test of the truncating feature in EDCZ&trade; please <span>use</span> with"),
              ("This is a test of the truncating features in EDCZ please use <span>with</span> caution <span>more with</span>.", 65,
               "This is a test of the truncating features in EDCZ please use <span>with</span>"),
              ("This is a test of the truncating features in EDCZ please use <span>with caution</span>", 65,
               "This is a test of the truncating features in EDCZ please use <span>with</span>"),
              ("<span>This</span> is a test of the truncating features in EDCZ please use <span>with caution</span>", 65,
               "<span>This</span> is a test of the truncating features in EDCZ please use <span>with</span>"),
              ("And this baby right here is the special last line that get's chopped a little shorter", 55,
               "And this baby right here is the special last line that "),
              ("This <span\nclass=\"hello\" id=\"id\">tag</span> is split by a new line just after the tag name", 7,
               "This <span\nclass=\"hello\" id=\"id\">ta</span>"),
              ("This <span\nclass=\"hello\" id=\"id\">tag</span> is split by a new line just after the tag name", 17,
               "This <span\nclass=\"hello\" id=\"id\">tag</span> is split"),
              ("These tags: <b >space</b>, <b\t>tab</b>, <b\n>LF</b>, <b\r>CR</b>, <b\f>FF</b>, are split by all the admissible whitespace characters just after the tag name", 45,
               "These tags: <b >space</b>, <b\t>tab</b>, <b\n>LF</b>, <b\r>CR</b>, <b\f>FF</b>, are split") )

    def testTruncation(self):
        for input, count, output in self.cases:
            self.assertEqual( htmltruncate.truncate(input, count), output )

    def testUnbalanced(self):
        self.assertRaises( htmltruncate.UnbalancedError, htmltruncate.truncate, 'I am a <b>bad</strong> little string with unbalanced tags', 20 )

    def testEntity(self):
        self.assertEqual( htmltruncate.truncate( "I&apos;m one", 3 ), "I&apos;m" )

    def testSelfClosing(self):
        self.assertEqual( htmltruncate.truncate( "I need<br /> a break", 11 ), "I need<br /> a br" )

    def testEllipsis(self):
        self.assertEqual( htmltruncate.truncate('this <b>word</b> is bolded', 10, '...' ), "this <b>word</b> ...")

    def testSurrounding(self):
        self.assertEqual( htmltruncate.truncate('<p>this paragraph should be cut in half</p>', 11, '...' ), "<p>this paragr...</p>")

    def testVoidElements(self):
        self.assertEqual( htmltruncate.truncate( "<a href='http://www.example.com'>I need<br> a break</a> one more time.", 17 ), "<a href='http://www.example.com'>I need<br> a break</a> on" )

if __name__ == "__main__":
    unittest.main()
