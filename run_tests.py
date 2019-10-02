#!/bin/python3
import unittest
#from gradescope_utils.autograder_utils.decorators import weight
#from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner
import subprocess32 as subprocess

DICTFILE = "wordlist.txt"

class TestCasesAssignment1(unittest.TestCase):
    def setUp(self):
        pass

#    @weight(2)
    def test_arrival_fcfs(self):
        """checking single word entries"""
        testfile = "test1.txt"
        testsub = subprocess.Popen(["./a.out", testfile, DICTFILE], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = testsub.stdout.read().decode().strip().split('\n')
        failmsg = f"Test Failed: Incorrect number of misspelled words. Should show none, shows {len(output)}"
        self.assertTrue(len(output)==1, msg=failmsg)
        self.assertEqual(output[0], "", msg=failmsg)
        testfile = "test2.txt"
        testsub = subprocess.Popen(["./a.out", testfile, DICTFILE], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        expected = "Ethiiopian's"
        output = testsub.stdout.read().decode().strip().split('\n')
        failmsg = "Test Failed: Incorrect word in output."
        self.assertEqual(output[0].lower(), expected.lower())
        failmsg2 = f"Test Failed: Incorrect number of misspelled words."
        self.assertTrue(len(output) == 1, msg=failmsg2)
        testsub.terminate()

#    @weight(2)
    def test_arrival_sstf(self):
        """checking longer strings"""
        testfile = "test3.txt"
        testsub = subprocess.Popen(["./a.out", testfile, DICTFILE], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = testsub.stdout.read()
        output = output.decode().strip().split('\n')
        failmsg = f"Test Failed: Incorrect number of misspelled words."
        self.assertTrue(len(output) == 1, msg=failmsg)
        self.assertEqual(output[0],'', msg=failmsg)
        testfile = "test4.txt"
        testsub = subprocess.Popen(["./a.out", testfile, DICTFILE], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = testsub.stdout.read()
        output = output.decode().strip().split('\n')
        expected = ["fluffl", "wobbit", "uill"]
        self.assertTrue(len(expected) == 3)
        for thing in output:
            failmsg = f"Test Failed: Incrorrect word in output."
            self.assertTrue(thing.lower() in expected, msg=failmsg)
        testsub.terminate()

    #@weight(1)
    def test_arrival_look(self):
        """checking for non-English word."""
        testfile = "test5.txt"
        testsub = subprocess.Popen(["./a.out", testfile, DICTFILE], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = testsub.stdout.read().decode().strip().split('\n')
        expected = "caoimhín"
        
        self.assertTrue(len(output) == 1, msg=f"Test Failed: Incorrect number of misspelled words")
        self.assertEqual(output[0].lower(), expected, msg=f"Test Failed: Incrorrect word in output.")
        testsub.terminate()

    #@weight(2)
    def test_multi_line(self):
        """checking a file with multiple lines."""
        testfile = "test6.txt"
        testsub = subprocess.Popen(["./a.out", testfile, DICTFILE], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        expected = ["fluffl", "wobbit", "uill"]
        output = testsub.stdout.read().decode().strip().split('\n')
        i = 0
        for item in output:
            failmsg = f"Test Failed: Incrorrect word in output."
            self.assertEqual(output[i].lower(), expected[i], msg=failmsg)
            i += 1
        testsub.terminate()
    
    #@weight(3)
    def test_word_with_punct(self):
        """checking a word with punctuation in the middle."""
        testfile = "test10.txt"
        testsub = subprocess.Popen(["./a.out", testfile, DICTFILE], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        expected = "j.ust"
        output = testsub.stdout.read().decode().strip().split('\n')
        self.assertTrue(len(output) == 1, msg=f"Test Failed: Wrong number of incorrect words.")
        self.assertEqual(output[0].lower(), expected, msg=f"Test Failed: Got incorrect misspelled word.")
        testsub.terminate()

    #@weight(5)
    def test_completion_look(self):
        """checking for buffer overflow in the input file."""
        testfile = "test7.txt"
        testsub = subprocess.Popen(["./a.out", testfile, DICTFILE], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, err_output = testsub.communicate()
        err_output = err_output.decode()
        output = output.decode().strip().split('\n')
        code = testsub.wait()
        failmsg = "Test Failed: Buffer Overflow occured while reading input file"
        expected = "uill"
        self.assertNotEqual(code, -11, msg=failmsg)
        self.assertEqual(len(output),2)
        self.assertEqual(output[0].lower(), expected)
        for letter in output[-1]:
            self.assertEqual(letter.lower(), 'a')
        testsub.terminate()

    #@weight(5)
    #def test_buffer_overflow_(self):
    #    """Checking for a buffer overflow in the input file."""
    #    testfile = "test8.txt"
    #    testsub = subprocess.Popen(["./a.out", testfile, DICTFILE], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #    output = testsub.stdout.read().decode().strip().split('\n')
    #    self.assertEqual(len(output),1))
    #    for letter in 
    #    testsub.terminate()

    #@weight(5)
    def test_buffer_overflow_dictionary(self):
        """Checking for a buffer overflow in the dictionary file."""
        BADDICT = "bo_wordlist.txt"
        testfile = "test9.txt"
        testsub = subprocess.Popen(["./a.out", testfile, BADDICT], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        err_output = testsub.stderr.read().decode()
        output = testsub.stdout.read().decode().strip().split('\n')
        code = testsub.wait()
        failmsg = "Test Failed: Buffer overflow occured when reading dictionary file."
        expected = "wobbit"
        self.assertNotEqual(code, -11, msg=failmsg)
        self.assertEqual(output[0].lower(), expected, msg="Test Failed: Word incorrect.")
        testsub.terminate()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCasesAssignment1)
    unittest.main()
    #JSONTestRunner(visibility="visible").run(suite)
