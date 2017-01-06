gem 'minitest', '~> 5.4'
require 'minitest/autorun'
require_relative '../lib/bottles'

class BottlesTest < Minitest::Test
    def test_99bottles_verse
        expected = "99 bottles of beer on the wall, " +
                   "99 bottles of beer.\n" +
                   "Take one down and pass it around, " +
                   "98 bottles of beer on the wall.\n"
        assert_equal expected, Bottles.new.verse(99)
    end
    def test_3bottles_verse
        expected = "3 bottles of beer on the wall, " +
                   "3 bottles of beer.\n" +
                   "Take one down and pass it around, " +
                   "2 bottles of beer on the wall.\n"
        assert_equal expected, Bottles.new.verse(3)
    end
end
