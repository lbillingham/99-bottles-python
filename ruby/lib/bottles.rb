class Bottles

    def bottle_number_for(number)
        case number
        when 0
            BottleNumber0
        when 1
            BottleNumber1
        else
            BottleNumber
        end.new(number)
    end
    def verse(number)
        bottle_number = bottle_number_for(number)
        next_bottle_number = bottle_number_for(bottle_number.successor)
        "#{bottle_number}".capitalize +
        " of beer on the wall, " +
        "#{bottle_number} of beer.\n" +
        "#{bottle_number.action}" +
        "#{next_bottle_number} of beer on the wall.\n"
    end
    def verses(starting, ending)
        starting.downto(ending).map {|n| verse(n)}.join("\n")
    end
    def song()
        verses(99, 0)
    end
end


class BottleNumber
    attr_reader :number
    def initialize(number)
        @number = number
    end
    def to_s
        "#{quantity} #{container}"
    end
    def action
        "Take #{pronoun} down and pass it around, "
    end
    def container
        "bottles"
    end
    def pronoun
        "one"
    end
    def quantity
        number.to_s
    end
    def successor
        number-1
    end
end

class BottleNumber0 < BottleNumber
    def action
        "Go to the store and buy some more, "
    end
    def quantity
        "no more"
    end
    def successor
        99
    end
end

class BottleNumber1 < BottleNumber
    def container
        "bottle"
    end
    def pronoun
        "it"
    end
end
