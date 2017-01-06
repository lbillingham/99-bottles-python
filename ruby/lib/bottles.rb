class Bottles
    def verse(number)
        if number == 99
            n = 99
        else
            n = 3
        end
    "#{number} bottles of beer on the wall, " +
    "#{number} bottles of beer.\n" +
    "Take one down and pass it around, " +
    "#{number-1} bottles of beer on the wall.\n"
    end
end