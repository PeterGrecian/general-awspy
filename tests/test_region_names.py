import region_names

def test_code_to_name_typical():
    assert region_names.code_to_name('eu-west-1') == 'Ireland'
    assert region_names.code_to_name('us-east-1') == 'N. Virginia'

def test_code_to_name_invalid():
    assert region_names.code_to_name('not-a-region') is None

def test_name_to_code_typical():
    assert region_names.name_to_code('Ireland') == 'eu-west-1'
    assert region_names.name_to_code('London') == 'eu-west-2'

def test_name_to_code_invalid():
    assert region_names.name_to_code('NotARegionName') is None

def test_get_all_region_codes_type():
    codes = region_names.get_all_region_codes()
    assert isinstance(codes, list)
    # Optionally check for known canonical entries: uncomment the following line if AWS credentials are set up
    # assert 'eu-west-1' in codes

def test_demo_runs_silently(capsys):
    region_names.demo()
    output = capsys.readouterr().out
    assert "eu-west-1" in output or "Ireland" in output

