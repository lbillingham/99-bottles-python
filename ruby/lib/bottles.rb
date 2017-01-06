class Bottles

    def pluralize(number)
        "bottle#{'s' unless (number-1) == 1}"
    end

    def verse(number)
    "#{number} bottles of beer on the wall, " +
    "#{number} bottles of beer.\n" +
    "Take one down and pass it around, " +
    "#{number-1} #{pluralize(number)} of beer " +
    "on the wall.\n"
    end
end