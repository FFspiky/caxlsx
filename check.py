from pathlib import Path
for version in ('base', 'corrected'):
    text = (Path('rendered') / (version + '.txt')).read_text()
    print(version, 'literal legend occurrences', text.count('R&D <budget>'),
          'cell label occurrences', text.count('Series & A'))
    if version == 'corrected':
        assert 'R&D <budget>' in text
        assert text.count('Series & A') >= 2
