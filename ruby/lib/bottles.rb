class Bottles

    def verse(number)
        case number
        when 0
            "#{quantity(number).capitalize} bottles of beer on the wall, " +
            "#{quantity(number)} bottles of beer.\n" +
            "Go to the store and buy some more, " +
            "99 bottles of beer on the wall.\n"
        else
            "#{quantity(number).capitalize} #{container(number)} of beer on the wall, " +
            "#{quantity(number)} #{container(number)} of beer.\n" +
            "Take #{pronoun(number)} down and pass it around, " +
            "#{quantity(number-1)} #{container(number-1)} of beer on the wall.\n"
        end
    end

    def verses(starting, ending)
        starting.downto(ending).map {|n| verse(n)}.join("\n")
    end

    def song()
        verses(99, 0)
    end

    def container(number)
        if number == 1
            "bottle"
        else
            "bottles"
        end
    end

    def pronoun(number)
        if number == 1
            "it"
        else
            "one"
        end
    end

    def quantity(number)
        if number == 0
            "no more"
        else
            number.to_s
        end
    end
end