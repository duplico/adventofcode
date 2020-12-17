# For some reason this one was really difficult to wrap my head
# around.

def mem_game()
     turn = 1
     turn_said = {}
     number_said_prev = nil
     number_said = nil

     starting_numbers = [14,1,17,0,3,20]

     starting_numbers.each do |starting_number|
          number_said = starting_number
          if number_said_prev != nil
               turn_said[number_said_prev] = turn - 1
          end

          number_said_prev = number_said
          turn +=1 
     end

     while turn <= 30000000
          # Someone just said number_said_prev.
          #  If it's been said before, we say the difference 
          #   between turn-1 and when it was said before.
          #  Then we update its last time said to turn-1.
          number_said_prev = number_said
          if turn_said[number_said_prev] != nil
               number_said = (turn-1)-turn_said[number_said_prev]
          else
               # The number said on turn turn-1 was never said before, so we
               #  say 0.
               number_said = 0
               turn_said[number_said_prev] = turn-1
          end
          
          turn_said[number_said_prev] = turn-1
          # puts number_said
          turn+=1
     end

     puts number_said
end

if __FILE__ == $0
     mem_game()
end
