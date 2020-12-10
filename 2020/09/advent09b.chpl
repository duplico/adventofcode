prototype module Advent09a {
     use IO;
     use DistributedDeque;

     config const invalid_value : int = 127;
     config const input_path : string = "sample_input.txt";

     var input_file : file;

     proc xmas_weakness() : int {
          // We'll use a queue for this.
          var deque = new DistDeque(int);
          
          var total = 0;           // Running total of the queue contents.
          var next_value : int;    // The current value we're either adding or dropping.
          var has_elem : bool;     // Tells us whether the queue still has values.
          
          input_file = open(input_path, iomode.r);
          
          var file_reader = input_file.reader();

          // Loop until the queue contents total to the target value.
          while (total != invalid_value) {
               if total < invalid_value {
                    // If our running total is less than target, then we need
                    //  to read the next value from the file. Add it to our
                    //  total, and enqueue it.
                    file_reader.read(next_value);
                    total += next_value;
                    deque.enqueue(next_value);
               } else {
                    // If our running total is now too high, then we need to
                    //  lower it by throwing away older values from the start
                    //  of our queue. Dequeue a value and subtract it from the
                    //  running total.
                    (has_elem, next_value) = deque.dequeue();
                    if !has_elem {
                         // We ran out of values in the queue. Error.
                         exit(1);
                    }
                    total -= next_value;
               }
          }

          input_file.close();

          // Now we have a queue full of the relevant values. We need to
          //  find the highest and lowest values in the queue. They are not
          //  necessarily in any particular order. So we'll do a linear search.

          var low : int = invalid_value;
          var high : int = 0;

          for next_value in deque.these(Ordering.FIFO) {
               if next_value < low then
                    low = next_value;
               if next_value > high then
                    high = next_value;
          }

          // Got it!
          return low + high;
     }

     proc main() {
          writeln("XMAS weakness found: ", xmas_weakness());
     }
}
