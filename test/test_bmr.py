import sys
sys.path.append("..")
import bmr

def test_bmr_imperial(capsys):
    input_values = ["female", 26, "imperial",
                    140, 5, 0, "sedentary", "Yes", .1]

    def mock_input(s):
        print(s, end='')
        return input_values.pop(0)
    bmr.input = mock_input

    bmr.main(debug=True)

    out, err = capsys.readouterr()

    # assert out == ''
    assert err == ''
    open("out_imperial.txt", "w").write(out)


def test_bmr_metric(capsys):
    input_values = ["male", 33, "metric", 90, 150, "light", "No"]

    def mock_input(s):
        print(s, end='')
        return input_values.pop(0)
    bmr.input = mock_input

    bmr.main(debug=True)

    out, err = capsys.readouterr()

    # assert out == ''
    assert err == ''
    open("out_metric.txt", "w").write(out)
