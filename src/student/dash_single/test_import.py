from student.dash_single.charts_creation import line_chart

def test_import():
    try:
        line_fig = line_chart("sports")  # Create line chart for sports

        print("Import successful, line chart created.")
    except Exception as e:
        print(f"Import failed: {e}")

if __name__ == "__main__":  # Entry point for the script

    test_import()
