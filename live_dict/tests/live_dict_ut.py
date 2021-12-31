from live_dict.live_dict import Screen

if __name__ == "__main__":
    data = {
        "bms1":
        {
            "pack":
            {
                "voltage": 132.0,
                "current": 0.367
            },
            "cells":
            {
                "1":
                {
                    "voltage": 3.4
                },
                "2":
                {
                    "voltage": 3.3
                }
            }

        },
        "flight_computer1":
        {
            "pedals":
            {
                "accel": 0.10,
                "brake": 0.0
            }
        },
        "bms2":
        {
            "pack":
            {
                "voltage": 132.0,
                "current": 0.367
            },
            "cells":
            {
                "1":
                {
                    "voltage": 3.4
                },
                "2":
                {
                    "voltage": 3.3
                }
            }

        },
        "flight_computer2":
        {
            "pedals":
            {
                "accel": 0.10,
                "brake": 0.0
            }
        },
        "bms3":
        {
            "pack":
            {
                "voltage": 132.0,
                "current": 0.367
            },
            "cells":
            {
                "1":
                {
                    "voltage": 3.4
                },
                "2":
                {
                    "voltage": 3.3
                }
            }

        },
        "flight_computer3":
        {
            "pedals":
            {
                "accel": 0.10,
                "brake": 0.0
            }
        },
        "bms4":
        {
            "pack":
            {
                "voltage": 132.0,
                "current": 0.367
            },
            "cells":
            {
                "1":
                {
                    "voltage": 3.4
                },
                "2":
                {
                    "voltage": 3.3
                }
            }

        },
        "flight_computer4":
        {
            "pedals":
            {
                "accel": 0.10,
                "brake": 0.0
            }
        },
    }

    screen = Screen(data)
    screen.run()
