from typing import Dict, List

# Hard coded for now. TODO: Refactor to be dynamic
FILES = ["..\\data\\25m@10s.txt", "..\\data\\50m@10s.txt", "..\\data\\25m@15s.txt",
         "..\\data\\50m@15s.txt"]

PLOT_TITLES: Dict[str, str] = {
    "25m50m@10s": "SEE index at 25m and 50m <br> Influence of current and wave (10s wave period)",
    "25m50m@15s": "SEE index at 25m and 50m <br> Influence of current and wave (15s wave period)",
    "25m@10s15s": "SEE index at 25m <br> Influence of current and wave (10s and 15s wave period)",
    "50m@10s15s": "SEE index at 50m <br> Influence of current and wave (10s and 15s wave period)",
}

AXIS_TITLES = [
    "Wave Height [m]",
    "Current Speed [m/s]",
    "SEE index"
]

COLOR_SCALES: dict[str, List[str]] = {
    'RCB_Set3_12': [
        "#8DD3C7",
        "#FFFFB3",
        "#BEBADA",
        "#FB8072",
        "#80B1D3",
        "#FDB462",
        "#B3DE69",
        "#FCCDE5",
        "#D9D9D9",
        "#BC80BD",
        "#CCEBC5",
        "#FFED6F",
    ],
    'R_rainbow_10': [
        "#FF0000",
        "#FF9900",
        "#CCFF00",
        "#33FF00",
        "#00FF66",
        "#00FFFF",
        "#0066FF",
        "#3300FF",
        "#CC00FF",
        "#FF0099",
    ]
}
