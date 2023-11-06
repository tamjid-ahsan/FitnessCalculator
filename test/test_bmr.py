import sys
sys.path.append("..")

import bmr
    
def test_bmr_imperial(capsys):
    input_values = ["male", 33, "imperial", 205, 5, 7, "sedentary", "Yes", .1]
    # input_values = ["male", 33, "metric", 90, 150, "light", "No"]
    
    def mock_input(s):
        print(s, end='')
        return input_values.pop(0)
    bmr.input = mock_input
    
    bmr.main()
    
    out, err = capsys.readouterr()
    
    # assert out == 'The result is 5\n'
    assert err == ''
    open("out_imperial.txt", "w").write(out)
    
def test_bmr_metric(capsys):
    # input_values = ["male", 33, "imperial", 205, 5, 7, "sedentary", "Yes", .1]
    input_values = ["male", 33, "metric", 90, 150, "light", "No"]
    
    def mock_input(s):
        print(s, end='')
        return input_values.pop(0)
    bmr.input = mock_input
    
    bmr.main()
    
    out, err = capsys.readouterr()
    
    # assert out == 'The result is 5\n'
    assert err == ''
    open("out_metric.txt", "w").write(out)