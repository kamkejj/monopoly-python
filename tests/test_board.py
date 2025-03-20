# Write a test for the Board class

from models.board import Board


def test_board():
    """Test the initialization and connectivity of the Monopoly board.

    Verifies:
    - Board initialization
    - Start position exists
    - Correct sequence of first x number of properties/spaces
    """
    # Setup
    board = Board()
    current_position = board.start

    # Test start position
    assert current_position is not None
    assert current_position.value.name == "Go"

    # Expected properties in order
    expected_properties = [
        "Go",
        "Mediteranean Avenue",
        "Community Chest",
        "Baltic Avenue",
        "Income Tax",
        "Reading Railroad",
        "Oriental Avenue",
        "Vermont Avenue",
        "Connecticut Avenue",
        "Jail",
        "St. Charles Place",
        "Electric Company",
        "States Avenue",
        "Virginia Avenue",
        "Pennsylvania Railroad"
    ]

    # Verify property sequence
    for expected_name in expected_properties[1:]:  # Skip "Go" as it's already checked
        current_position = current_position.next
        assert current_position.value.name == expected_name

