class Bottles

    def verse(number)
        bottle_number = BottleNumber.new(number)
        "#{bottle_number.quantity.capitalize} #{bottle_number.container} of beer on the wall, " +
        "#{bottle_number.quantity} #{bottle_number.container} of beer.\n" +
        "#{bottle_number.action}" +
        "#{quantity(sucessor(number))} #{container(sucessor(number))} of beer on the wall.\n"
    end


    def verses(starting, ending)
        starting.downto(ending).map {|n| verse(n)}.join("\n")
    end

    def song()
        verses(99, 0)
    end

    def container(number)
        BottleNumber.new(number).container
    end

    def quantity(number)
        BottleNumber.new(number).quantity
    end

    def action(number)
        BottleNumber.new(number).action
    end
    def sucessor(number)
        BottleNumber.new(number).sucessor
    end
end


class BottleNumber
    attr_reader :number
    def initialize(number)
        @number = number
    end
    def action
        if number == 0
            "Go to the store and buy some more, "
        else
            "Take #{pronoun} down and pass it around, "
        end
    end
    def container
        if number == 1
            "bottle"
        else
            "bottles"
        end
    end
    def pronoun
        if number == 1
            "it"
        else
            "one"
        end
    end
    def quantity
        if number == 0
            "no more"
        else
            number.to_s
        end
    end
    def sucessor
        if number == 0
            99
        else
            number-1
        end
    end
end
