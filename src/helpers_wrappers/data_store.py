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
        # "#33FF00",
        "#00FF66",
        # "#00FFFF",
        "#0066FF",
        "#3300FF",
        "#CC00FF",
        "#FF0099",
    ],
    'D3': [
        "#1f77b4",
        "#ff7f0e",
        "#2ca02c",
        "#d62728",
        "#9467bd",
        "#8c564b",
        "#e377c2",
        "#7f7f7f",
        "#bcbd22",
        "#17becf",
    ],
    'Plotly': [
        "#636efa",
        "#EF553B",
        "#00cc96",
        "#ab63fa",
        "#FFA15A",
        "#19d3f3",
        "#FF6692",
        "#B6E880",
        "#FF97FF",
        "#FECB52",
    ],
    'G10': [
        "#3366CC",
        "#DC3912",
        "#FF9900",
        "#109618",
        "#990099",
        "#3B3EAC",
        "#0099C6",
        "#DD4477",
        "#66AA00",
        "#B82E2E",
    ],
    'Set1': [
        "#e41a1c",
        "#377eb8",
        "#4daf4a",
        "#984ea3",
        "#ff7f00",
        "#ffff33",
        "#a65628",
        "#f781bf",
        "#999999",
    ],
    'Light24': ['#FD3216', '#00FE35', '#6A76FC', '#FED4C4', '#FE00CE', '#0DF9FF', '#F6F926',
                '#FF9616', '#479B55', '#EEA6FB', '#DC587D', '#D626FF', '#6E899C', '#00B5F7',
                '#B68E00', '#C9FBE5', '#FF0092', '#22FFA7', '#E3EE9E', '#86CE00', '#BC7196',
                '#7E7DCD', '#FC6955', '#E48F72'],
    'Vivid': ['rgb(229, 134, 6)', 'rgb(93, 105, 177)', 'rgb(82, 188, 163)', 'rgb(153, 201, 69)',
              'rgb(204, 97, 176)', 'rgb(36, 121, 108)', 'rgb(218, 165, 27)', 'rgb(47, 138, 196)',
              'rgb(118, 78, 159)', 'rgb(237, 100, 90)', 'rgb(165, 170, 153)'],
    'Pastel': ['rgb(102, 197, 204)', 'rgb(246, 207, 113)', 'rgb(248, 156, 116)',
               'rgb(220, 176, 242)', 'rgb(135, 197, 95)', 'rgb(158, 185, 243)',
               'rgb(254, 136, 177)', 'rgb(201, 219, 116)', 'rgb(139, 224, 164)',
               'rgb(180, 151, 231)', 'rgb(179, 179, 179)']

}
