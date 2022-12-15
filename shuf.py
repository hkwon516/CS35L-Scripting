#!/usr/local/cs/bin/python3.10

import random, sys 
import argparse, string

# Hannah Kwon 
# 705182275


"""
Your program should also support zero non-option args or a single non-option "-" 
or a single non-option argument other than '-' 
Your program should report an error if given invalid args.
Don't forget to change its usage message to accurately describe the modified behavior.

"""

#how to shuffle files 
# 1. Read a file 
# 2. Parse them line by line -write them in a text
# 3. And then shuffle 

class Shuffle : 
    def __init__(self, filename) : 
        # if filename is not None and filename != "=" :
        #     f = open(filename, 'r')
        f = open(filename,'r') if filename is not None and filename != "-" else sys.stdin
        self.lines = f.readlines() 
        f.close()


        # self.input = sys.stdin.readlines()

        self.num_lines = len(self.lines)
        self.total_lines = list(range(0, len(self.lines))) #have a list of numbers from 0 - total lines
        random.shuffle(self.total_lines)

        self.total_lines1 = list(range(0, len(self.lines)))
        self.rand_arr = random.sample(self.total_lines1, len(self.total_lines1))

        # Set inputs based on flag arguments 
        # if echo : 


    def shuffle(self) :
        # should sys.stdout.write out each line only only once 
        # currently sys.stdout.writes out duplicates

        for i in range(self.num_lines) :
            sys.stdout.write(self.lines[self.total_lines[i]])
    
    def shuffle_with_nums(self, num) :
        # should sys.stdout.write out each line only only once 
        # currently sys.stdout.writes out duplicates
        for i in range(min(num, self.num_lines)):
            sys.stdout.write(self.lines[self.total_lines[i]])
    
    def shuffle_with_dups(self, num, repeat = False) :
        if repeat == False : 
            for i in range(min(num, self.num_lines)):
                sys.stdout.write(self.lines[random.choice(self.total_lines)])
        else : 
            while True : 
                sys.stdout.write(self.lines[random.choice(self.total_lines)])
    
    def shuffle_without_dups(self, num) :
        for i in range(num):
            sys.stdout.write(self.lines[self.rand_arr[i]])


        
# read from stdin       

def main() : 
    # Initializing parser 
    parser = argparse.ArgumentParser()  #create ArgumentParser Object which holds all the info necessary to parse the command line into Python data types
    parser.add_argument('-e', '--echo',  help = 'treat each ARG as an input line', nargs = '*')
    parser.add_argument('-i', '--input-range', type = str, help = 'treat each number LO through HI as an input line')
    parser.add_argument('-n', '--head-count', type = int, help = 'output at most COUNT lines')
    parser.add_argument('-r','--repeat',  help = 'output lines can be repeated', action = 'store_true')
    parser.add_argument('filename', help = 'put in filename',  const = False, nargs = '?')

    args = parser.parse_args() #non_args is a list
    
    match vars(args) : 
        #throw errors
        case {"echo" : echo ,"input_range" : num_range} if echo is not None and num_range is not None: 
            sys.stdout.write("shuf.py: cannot combine -e and -i options")
        #commands
        case {"echo" : echo, "head_count" : head_count, "repeat" : repeat} if echo is not None and head_count is None and repeat == False: 
            for out in random.sample(echo, len(echo)) :
                    sys.stdout.write (out+  "\n")
        case {"echo" : echo, "head_count" : head_count, "repeat" : repeat} if echo is not None and head_count is None and repeat == True: 
            while True : 
                    sys.stdout.write(random.choice(echo)+  "\n") #repeat forever
        case {"echo" : echo, "head_count" : head_count, "repeat" : repeat} if echo is not None and head_count is not None and repeat == True: 
            for i in range(head_count) :
                 sys.stdout.write(random.choice(echo)+  "\n")
        case {"echo" : echo, "head_count" : head_count, "repeat" : repeat} if echo is not None and head_count is not None and repeat == False:
            random_arr = random.sample(echo, len(echo))
            for i in range(min(head_count, len(random_arr))) :
                 sys.stdout.write(random_arr[i] +  "\n")
        case {"input_range" : input_range, "head_count" : head_count, "repeat" :repeat} if repeat == True and head_count is not None and input_range is not None: 
            output_range = input_range.split('-')
            output_file = list(range(int(output_range[0]), int(output_range[1])+1))
            random_arr = random.sample(output_file, len(output_file))
            for i in range(head_count):
                sys.stdout.write(str(random.choice(random_arr))+ '\n')
            # for i in range(min(head_count, len(random_arr))) :
            #      sys.stdout.write(random_arr[i])
        case {"input_range" : input_range, "repeat" :repeat} if repeat == True and input_range is not None: 
            input_range = input_range.split('-')
            output_file = list(range(int(input_range[0]), int(input_range[1])+1))
            random_arr = random.sample(output_file, len(output_file))
            while True : 
                sys.stdout.write(str(random.choice(random_arr))+'\n')
        case {"input_range" : input_range, "head_count" : head_count} if input_range is not None : 
            input_range = input_range.split('-')
            output_file = list(range(int(input_range[0]), int(input_range[1])+1))
            random_arr = random.sample(output_file, len(output_file))
            if head_count is None :
                for i in range(len(random_arr)) :
                    sys.stdout.write(str(random_arr[i]) + '\n')
            else : 
                for i in range(min(head_count, len(random_arr))) :
                    sys.stdout.write(str(random_arr[i]) + '\n')
            
        case {"filename" : filename, "head_count" : head_count, "repeat" :repeat} if head_count is not None and repeat is True:
            # for i in range (head_count):
            s = Shuffle(filename)
            s.shuffle_with_dups(head_count)
        case {"filename" : filename, "head_count" : head_count, "repeat" :repeat} if head_count is None and repeat is True:
            
            s = Shuffle(filename)
            s.shuffle_with_dups(float('inf'), True)
        #repeat
        case {"filename" : filename, "head_count" : head_count, "repeat" :repeat} if head_count is None and repeat is False:
        
            # s = Shuffle(filename)
            # if s is None : 
            #     #reading from stdin
            # else : 
            s = Shuffle(filename)
            s.shuffle()

        case {"filename" : filename, "head_count" : head_count, "repeat" :repeat} if head_count is not None and repeat is False:
            s = Shuffle(filename)
            s.shuffle_with_nums(head_count) 
        

   
#running from the command line    
if __name__ == "__main__":
    main()









