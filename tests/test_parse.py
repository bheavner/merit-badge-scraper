from scraper.parse import parse_badge_index, parse_requirements

def test_parse_badge_index():
    html = """
    <a href="/skills/merit-badges/camping/">Camping</a>
    <a href="/skills/merit-badges/citizenship-in-society/">Citizenship</a>
    """
    badges = parse_badge_index(html)
    assert "Camping" in badges
    assert "Citizenship" in badges

def test_parse_requirements():
    html = """
    <ol>
      <li>Do requirement 1.</li>
      <li>Do requirement 2.</li>
    </ol>
    """
    reqs = parse_requirements(html)
    assert reqs == ["Do requirement 1.", "Do requirement 2."]

