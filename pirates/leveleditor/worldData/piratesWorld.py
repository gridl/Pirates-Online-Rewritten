from pandac.PandaModules import Point3, VBase3, Vec4, Vec3
objectStruct = {
    'AmbientColors': {
        0: Vec4(0.207843, 0.243137, 0.447059, 1),
        2: Vec4(0.666667, 0.721569, 0.792157, 1),
        4: Vec4(0.721569, 0.611765, 0.619608, 1),
        6: Vec4(0.207843, 0.243137, 0.447059, 1),
        8: Vec4(0.384314, 0.419608, 0.564706, 1)
    },
    'DirectionalColors': {
        0: Vec4(0.956863, 0.909804, 0.894118, 1),
        2: Vec4(1, 1, 1, 1),
        4: Vec4(0.439216, 0.176471, 0, 1),
        6: Vec4(0.513726, 0.482353, 0.639216, 1),
        8: Vec4(0.447059, 0.439216, 0.537255, 1)
    },
    'FogColors': {
        0: Vec4(0.172549, 0.180392, 0.290196, 1),
        2: Vec4(0.894118, 0.894118, 1, 1),
        4: Vec4(0.231373, 0.203922, 0.184314, 1),
        6: Vec4(0.172549, 0.180392, 0.290196, 1),
        8: Vec4(0.129412, 0.137255, 0.203922, 1)
    },
    'FogRanges': {
        0: 0.000699999975040555,
        2: 0.00019999999494757503,
        4: 0.00039999998989515007,
        6: 0.000699999975040555,
        8: 0.0
    },
    'Objects': {
        '1141410776.53sdnaik': {
            'Type': 'Region',
            'Name': 'default',
            'Objects': {
                '1150922126.8dzlu': {
                    'Type': 'Island',
                    'Name': 'Port Royal',
                    'File': 'PortRoyalIsland',
                    'Environment': 'Interior',
                    'Hpr': Point3(-180.0, 0.0, 0.0),
                    'Minimap': False,
                    'Objects': {
                        '1157060429.94sdnaik': {
                            'Type': 'LOD Sphere',
                            'Hpr': VBase3(136.467, 0.0, 0.0),
                            'Pos': Point3(524.742, 2115.765, 580.947),
                            'Radi': [4500.0, 5000.0, 7500.0],
                            'Scale': VBase3(1.0, 1.0, 1.0),
                            'VisSize': ''
                        }
                    },
                    'Pos': Point3(-186.051, 1925.536, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Undockable': False,
                    'VisSize': '',
                    'Visibility': 'Grid',
                    'Visual': {
                        'Model': 'models/islands/pir_m_are_isl_portRoyal'
                    }
                },
                '1156207188.95dzlu': {
                    'Type': 'Island',
                    'Name': 'Tortuga',
                    'File': 'tortugaIsland',
                    'Hpr': VBase3(-180.0, 0.0, 0.0),
                    'Minimap': False,
                    'Objects': {
                        '1158214327.11sdnaik': {
                            'Type': 'LOD Sphere',
                            'Hpr': Point3(0.0, 0.0, 0.0),
                            'Pos': Point3(-166.294, -732.313, 210.853),
                            'Radi': [2700.0, 3200.0, 6000.0],
                            'Scale': VBase3(1.0, 1.0, 1.0),
                            'VisSize': ''
                        }
                    },
                    'Phase': 1,
                    'Pos': Point3(10568.492, 16760.082, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Undockable': False,
                    'VisSize': '',
                    'Visual': {
                        'Model': 'models/islands/pir_m_are_isl_tortuga'
                    }
                },
                '1264624291.62caoconno': {
                    'Type': 'Island',
                    'Name': 'Mysterious Island',
                    'File': 'MysteriousIsland_08',
                    'Hpr': VBase3(-180.0, 0.0, 0.0),
                    'Minimap': False,
                    'Objects': {
                        '1158214327.11sdnaik': {
                            'Type': 'LOD Sphere',
                            'Hpr': Point3(0.0, 0.0, 0.0),
                            'Pos': Point3(-166.294, -732.312, 210.853),
                            'Radi': [
                                2700.0,
                                3200.0,
                                6000.0],
                            'Scale': VBase3(1.0, 1.0, 1.0),
                            'VisSize': '' } },
                    'Phase': 1,
                    'Pos': Point3(8568.492, 30760.0819, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Undockable': True,
                    'VisSize': '',
                    'Visual': {
                        'Model': 'models/islands/pir_m_are_isl_mysterious_08' } },
                '1150922126.828659a2': {
                    'Type': 'Island',
                    'Name': 'Nassau',
                    'File': 'NassauIsland',
                    'Hpr': VBase3(-180.0, 0.0, 0.0),
                    'Minimap': False,
                    'Objects': {
                        '1158214327.828659a2': {
                            'Type': 'LOD Sphere',
                            'Hpr': Point3(0.0, 0.0, 0.0),
                            'Pos': Point3(-166.294, -732.312, 210.853),
                            'Radi': [11520, 12520, 13520],
                            'Scale': VBase3(1.0, 1.0, 1.0),
                            'VisSize': '' } },
                    'Phase': 1,
                    'Pos': Point3(-18568.492, -30760.0819, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Undockable': True,
                    'VisSize': '',
                    'Visual': {
                        'Model': 'models/islands/pir_m_are_isl_nassau' } },                
                '1156359855.24bbathen': {
                    'Type': 'Island',
                    'Name': 'Isla Cangrejos',
                    'File': 'CangrejosIsland',
                    'Environment': 'Interior',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Minimap': False,
                    'Objects': {
                        '1158296490.13sdnaik': {
                            'Type': 'LOD Sphere',
                            'Hpr': Point3(0.0, 0.0, 0.0),
                            'Pos': Point3(-40.882, 79.287, 47.831),
                            'Radi': [700.0, 1100.0, 4500.0],
                            'Scale': VBase3(1.0, 1.0, 1.0),
                            'VisSize': ''
                        }
                    },
                    'Phase': 1,
                    'Pos': Point3(20199.543, 24930.109, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Undockable': False,
                    'VisSize': '',
                    'Visibility': 'Grid',
                    'Visual': {
                        'Model': 'models/islands/pir_m_are_isl_cangrejos'
                    }
                },
                '1159933206.48sdnaik': {
                    'Type': 'Island',
                    'Name': 'Kingshead',
                    'File': 'KingsheadIsland',
                    'Environment': 'Interior',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Minimap': False,
                    'Objects': {
                        '1162600600.5sdnaik': {
                            'Type': 'LOD Sphere',
                            'Hpr': Point3(0.0, 0.0, 0.0),
                            'Pos': Point3(-96.153, -25.37, 136.443),
                            'Radi': [1550.0, 2100.0, 6000.0],
                            'Scale': VBase3(1.0, 1.0, 1.0),
                            'VisSize': ''
                        }
                    },
                    'Phase': 1,
                    'Pos': Point3(21048.535, -12029.463, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Undockable': False,
                    'VisSize': '',
                    'Visibility': 'Grid',
                    'Visual': {
                        'Model': 'models/islands/pir_m_are_isl_kingshead'
                    }
                },
                '1160614528.73sdnaik': {
                    'Type': 'Island',
                    'Name': 'Cuba',
                    'File': 'CubaIsland',
                    'Environment': 'Interior',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Minimap': False,
                    'Objects': {
                        '1163119750.53sdnaik': {
                            'Type': 'LOD Sphere',
                            'Hpr': Point3(0.0, 0.0, 0.0),
                            'Pos': Point3(154.735, 0.0, 121.512),
                            'Radi': [2200.0, 2700.0, 7000.0],
                            'Scale': VBase3(1.0, 1.0, 1.0),
                            'VisSize': ''
                        }
                    },
                    'Phase': 1,
                    'Pos': Point3(-16098.668, 1857.619, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Undockable': False,
                    'VisSize': '',
                    'Visibility': 'Grid',
                    'Visual': {
                        'Model': 'models/islands/pir_m_are_isl_cuba'
                    }
                },
                '1161282725.84kmuller': {
                    'Type': 'Island',
                    'Name': "Rumrunner's Isle",
                    'File': 'RumrunnerIsland',
                    'Hpr': VBase3(0.0, 0.0, 0.0),
                    'Minimap': False,
                    'Objects': {
                        '1161664293.39sdnaik': {
                            'Type': 'LOD Sphere',
                            'Hpr': Point3(0.0, 0.0, 0.0),
                            'Pos': Point3(-3.644, 24.436, -0.33),
                            'Radi': [800.0, 1200.0, 4500.0],
                            'Scale': VBase3(1.0, 1.0, 1.0),
                            'VisSize': ''
                        }
                    },
                    'Phase': 1,
                    'Pos': Point3(656.261, 21799.172, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Undockable': False,
                    'VisSize': '',
                    'Visual': {
                        'Model': 'models/islands/pir_m_are_isl_rumRunner'
                    }
                },
                '1164135492.81dzlu': {
                    'Type': 'Island',
                    'Name': "Devil's Anvil",
                    'File': 'AnvilIsland',
                    'Environment': 'Interior',
                    'Hpr': VBase3(0.0, 0.0, 0.0),
                    'Minimap': False,
                    'Objects': {
                        '1164760719.72sdnaik': {
                            'Type': 'LOD Sphere',
                            'Hpr': Point3(0.0, 0.0, 0.0),
                            'Pos': Point3(-51.333, -49.722, 287.083),
                            'Radi': [800.0, 1300.0, 4500.0],
                            'Scale': VBase3(1.0, 1.0, 1.0),
                            'VisSize': ''
                        }
                    },
                    'Phase': 1,
                    'Pos': Point3(9109.271, 7179.465, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Undockable': False,
                    'VisSize': '',
                    'Visibility': 'Grid',
                    'Visual': {
                        'Model': 'models/islands/pir_m_are_isl_devilsAnvil'
                    }
                },
                '1164150392.42dzlu': {
                    'Type': 'Island',
                    'Name': 'Isla Tormenta',
                    'File': 'TormentaIsland',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Objects': {
                        '1173381974.5sdnaik': {
                            'Type': 'LOD Sphere',
                            'Hpr': Point3(0.0, 0.0, 0.0),
                            'Pos': Point3(616.474, 321.018, -18.171),
                            'Radi': [1800.0, 2300.0, 4500.0],
                            'Scale': VBase3(1.0, 1.0, 1.0),
                            'VisSize': ''
                        }
                    },
                    'Phase': 1,
                    'Pos': Point3(-16722.863, -10071.313, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Undockable': False,
                    'Visual': {
                        'Model': 'models/islands/pir_m_are_isl_tormenta'
                    }
                },
                '1164157132.99dzlu': {
                    'Type': 'Island',
                    'Name': 'Isla Perdida',
                    'File': 'PerdidaIsland',
                    'Environment': 'Interior',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Minimap': False,
                    'Objects': {
                        '1164763977.22sdnaik': {
                            'Type': 'LOD Sphere',
                            'Hpr': Point3(0.0, 0.0, 0.0),
                            'Pos': Point3(-29.059, 204.24, 439.628),
                            'Radi': [1300.0, 1800.0, 6000.0],
                            'Scale': VBase3(1.0, 1.0, 1.0),
                            'VisSize': ''
                        }
                    },
                    'Phase': 1,
                    'Pos': Point3(-20199.961, 18180.18, 0.32),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Undockable': False,
                    'VisSize': '',
                    'Visibility': 'Grid',
                    'Visual': {
                        'Model': 'models/islands/pir_m_are_isl_perdida'
                    }
                },
                '1164763706.66sdnaik': {
                    'Type': 'Island',
                    'Name': 'Driftwood Island',
                    'File': 'DriftwoodIsland',
                    'Environment': 'Interior',
                    'Hpr': VBase3(0.0, 0.0, 0.0),
                    'Minimap': False,
                    'Objects': {
                        '1164763735.42sdnaik': {
                            'Type': 'LOD Sphere',
                            'Hpr': Point3(0.0, 0.0, 0.0),
                            'Pos': Point3(-40.882, 79.287, 47.831),
                            'Radi': [650.0, 1100.0, 4500.0],
                            'Scale': VBase3(1.0, 1.0, 1.0),
                            'VisSize': ''
                        }
                    },
                    'Phase': 1,
                    'Pos': Point3(-9286.006, 11719.344, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Undockable': False,
                    'VisSize': '',
                    'Visibility': 'Grid',
                    'Visual': {
                        'Model': 'models/islands/pir_m_are_isl_driftwood'
                    }
                },
                '1173381952.2sdnaik': {
                    'Type': 'Island',
                    'Name': 'Outcast Isle',
                    'File': 'OutcastIsland',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Minimap': False,
                    'Objects': {
                        '1164760526.77sdnaik': {
                            'Type': 'LOD Sphere',
                            'Hpr': Point3(0.0, 0.0, 0.0),
                            'Pos': Point3(19.047, 304.658, 475.384),
                            'Radi': [700.0, 1100.0, 4500.0],
                            'Scale': VBase3(1.0, 1.0, 1.0),
                            'VisSize': ''
                        }
                    },
                    'Phase': 1,
                    'Pos': Point3(-10389.661, -19767.42, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Undockable': False,
                    'VisSize': '',
                    'Visual': {
                        'Model': 'models/islands/pir_m_are_isl_outcast'
                    }
                },
                '1173382404.64sdnaik': {
                    'Type': 'Island',
                    'Name': 'Cutthroat Isle',
                    'File': 'CutthroatIsland',
                    'Environment': 'Interior',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Minimap': False,
                    'Objects': {
                        '1173382432.38sdnaik': {
                            'Type': 'LOD Sphere',
                            'Hpr': Point3(0.0, 0.0, 0.0),
                            'Pos': Point3(82.898, 17.675, 160.281),
                            'Radi': [1200.0, 1600.0, 4500.0],
                            'Scale': VBase3(1.0, 1.0, 1.0),
                            'VisSize': ''
                        }
                    },
                    'Phase': 1,
                    'Pos': Point3(13299.626, -10296.977, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Undockable': False,
                    'VisSize': '',
                    'Visibility': 'Grid',
                    'Visual': {
                        'Model': 'models/islands/pir_m_are_isl_cutthroat'
                    }
                },
                '1185235968.0dxschafe0': {
                    'Type': 'Ship Spawn Node',
                    'Flagship': True,
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Level': '3',
                    'Pos': Point3(7536.718, 20771.877, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'NAVY_KINGFISHER',
                    'Team': 'default',
                    'Visual': {
                        'Color': (0, 0, 0.65, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1185235968.0dxschafe1': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-20005.879, 15829.349, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1185236224.0dxschafe': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-24653.135, -1986.28, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1185236224.0dxschafe3': {
                    'Type': 'Ship Spawn Node',
                    'Flagship': True,
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Level': '3',
                    'Pos': Point3(-20880.082, 16510.27, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'EITC_BARRACUDA',
                    'Team': 'default',
                    'Visual': {
                        'Color': (0, 0, 0.65, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1185236480.0dxschafe': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(18753.035, -13291.3, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1185236480.0dxschafe1': {
                    'Type': 'Ship Spawn Node',
                    'Flagship': True,
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Level': '3',
                    'Pos': Point3(22723.27, -11160.567, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'NAVY_MAN_O_WAR',
                    'Team': 'default',
                    'Visual': {
                        'Color': (0, 0, 0.65, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1185236736.0dxschafe': {
                    'Type': 'Ship Spawn Node',
                    'Flagship': True,
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Level': '3',
                    'Pos': Point3(-23213.016, -3726.756, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'EITC_SENTINEL',
                    'Team': 'default',
                    'Visual': {
                        'Color': (0, 0, 0.65, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1185236864.0dxschafe': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(15434.296, 23497.52, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1185237120.0dxschafe': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-25238.758, -5313.116, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1185237120.0dxschafe1': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-10399.86, -20861.783, 39.996),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1185237120.0dxschafe2': {
                    'Type': 'Ship Spawn Node',
                    'Flagship': True,
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Level': '3',
                    'Pos': Point3(-9856.596, -17695.881, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'NAVY_COLOSSUS',
                    'Team': 'default',
                    'Visual': {
                        'Color': (0, 0, 0.65, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1185237248.0dxschafe': {
                    'Type': 'Ship Spawn Node',
                    'Flagship': True,
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Level': '3',
                    'Pos': Point3(22025.379, -9170.477, 0.004),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'EITC_CORVETTE',
                    'Team': 'default',
                    'Visual': {
                        'Color': (0, 0, 0.65, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1196970035.53sdnaik': {
                    'Type': 'Island',
                    'Name': 'Isla de la Avaricia',
                    'File': 'pvpShipIsland2',
                    'Environment': 'Interior',
                    'Hpr': VBase3(0.0, 0.0, 0.0),
                    'Minimap': False,
                    'Objects': {
                        '1196970432.69sdnaik': {
                            'Type': 'LOD Sphere',
                            'Hpr': VBase3(-24.178, 0.0, 0.0),
                            'Pos': Point3(-1.631, -36.854, 0.254),
                            'Radi': [600.0, 1100.0, 4500.0],
                            'Scale': VBase3(1.0, 1.0, 1.0),
                            'VisSize': ''
                        }
                    },
                    'PVPTeam': 2,
                    'Pos': Point3(20505.961, -106.404, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Undockable': False,
                    'VisSize': '',
                    'Visibility': 'Grid',
                    'Visual': {
                        'Model': 'models/islands/pir_m_are_isl_pvpSpanish'
                    }
                },
                '1196970080.56sdnaik': {
                    'Type': 'Island',
                    'Name': "Ile d'Etable de Porc",
                    'File': 'pvpShipIsland1',
                    'Environment': 'Interior',
                    'Hpr': VBase3(0.0, 0.0, 0.0),
                    'Minimap': False,
                    'Objects': {
                        '1196970440.66sdnaik': {
                            'Type': 'LOD Sphere',
                            'Hpr': VBase3(155.709, 0.0, 0.0),
                            'Pos': Point3(70.641, -22.088, 0.0),
                            'Radi': [600.0, 1100.0, 4500.0],
                            'Scale': VBase3(1.0, 1.0, 1.0),
                            'VisSize': ''
                        }
                    },
                    'PVPTeam': 1,
                    'Pos': Point3(25429.918, 11463.408, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Undockable': False,
                    'VisSize': '',
                    'Visibility': 'Grid',
                    'Visual': {
                        'Model': 'models/islands/pir_m_are_isl_pvpFrench'
                    }
                },
                '1201636857.8kmuller': {
                    'Type': 'Island',
                    'File': 'pvp_rock_big_1',
                    'Environment': 'Interior',
                    'Hpr': VBase3(-44.631, 0.0, 0.0),
                    'Minimap': False,
                    'Objects': {
                        '1210981042.09kmuller': {
                            'Type': 'LOD Sphere',
                            'Hpr': Point3(0.0, 0.0, 0.0),
                            'Pos': Point3(68.294, 79.498, 0.0),
                            'Radi': [300.0, 1000.0, 3000.0],
                            'Scale': VBase3(1.0, 1.0, 1.0),
                            'VisSize': ''
                        }
                    },
                    'Pos': Point3(18809.854, 5488.201, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Undockable': True,
                    'VisSize': '',
                    'Visibility': 'Grid',
                    'Visual': {
                        'Model': 'models/islands/pir_m_are_isl_rockBig'
                    }
                },
                '1201641372.09kmuller': {
                    'Type': 'Island',
                    'File': 'pvp_rock_med_1',
                    'Environment': 'Interior',
                    'Hpr': VBase3(-22.62, 0.0, 0.0),
                    'Minimap': False,
                    'Objects': {
                        '1210981113.03kmuller': {
                            'Type': 'LOD Sphere',
                            'Hpr': Point3(0.0, 0.0, 0.0),
                            'Pos': Point3(47.431, 46.449, 0.0),
                            'Radi': [300.0, 1000.0, 3000.0],
                            'Scale': VBase3(1.0, 1.0, 1.0),
                            'VisSize': ''
                        }
                    },
                    'Pos': Point3(20269.568, 5435.323, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Undockable': True,
                    'VisSize': '',
                    'Visibility': 'Grid',
                    'Visual': {
                        'Model': 'models/islands/pir_m_are_isl_rockMed'
                    }
                },
                '1201641393.2kmuller': {
                    'Type': 'Island',
                    'File': 'pvp_rock_big_3',
                    'Environment': 'Interior',
                    'Hpr': VBase3(333.579, 0.0, 0.0),
                    'Minimap': False,
                    'Objects': {
                        '1210981144.78kmuller': {
                            'Type': 'LOD Sphere',
                            'Hpr': Point3(0.0, 0.0, 0.0),
                            'Pos': Point3(50.724, -12.372, 0.0),
                            'Radi': [300.0, 1000.0, 3000.0],
                            'Scale': VBase3(1.0, 1.0, 1.0),
                            'VisSize': ''
                        }
                    },
                    'Pos': Point3(25643.311, 5591.078, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Undockable': True,
                    'VisSize': '',
                    'Visibility': 'Grid',
                    'Visual': {
                        'Model': 'models/islands/pir_m_are_isl_rockBig'
                    }
                },
                '1201641405.3kmuller': {
                    'Type': 'Island',
                    'File': 'pvp_rock_med_2',
                    'Environment': 'Interior',
                    'Hpr': VBase3(163.401, 0.0, 0.0),
                    'Minimap': False,
                    'Objects': {
                        '1210981205.23kmuller': {
                            'Type': 'LOD Sphere',
                            'Hpr': Point3(0.0, 0.0, 0.0),
                            'Pos': Point3(20.789, 44.607, 0.0),
                            'Radi': [500.0, 1000.0, 3000.0],
                            'Scale': VBase3(0.511, 0.511, 0.511),
                            'VisSize': ''
                        }
                    },
                    'Pos': Point3(28189.699, 7544.893, 0.0),
                    'Scale': VBase3(1.956, 1.956, 1.956),
                    'Undockable': True,
                    'VisSize': '',
                    'Visibility': 'Grid',
                    'Visual': {
                        'Model': 'models/islands/pir_m_are_isl_rockMed'
                    }
                },
                '1201641438.69kmuller': {
                    'Type': 'Island',
                    'File': 'pvp_rock_big_2',
                    'Environment': 'Interior',
                    'Hpr': VBase3(140.533, 0.0, 0.0),
                    'Minimap': False,
                    'Objects': {
                        '1210981266.57kmuller': {
                            'Type': 'LOD Sphere',
                            'Hpr': Point3(0.0, 0.0, 0.0),
                            'Pos': Point3(50.724, -12.372, 0.0),
                            'Radi': [400.0, 1000.0, 3000.0],
                            'Scale': VBase3(1.0, 1.0, 1.0),
                            'VisSize': ''
                        }
                    },
                    'Pos': Point3(27261.391, 1133.732, 0.001),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Undockable': True,
                    'VisSize': '',
                    'Visibility': 'Grid',
                    'Visual': {
                        'Model': 'models/islands/pir_m_are_isl_rockBig'
                    }
                },
                '1201641487.41kmuller': {
                    'Type': 'Island',
                    'File': 'pvp_rock_sml_1',
                    'Environment': 'Interior',
                    'Hpr': VBase3(0.0, 0.0, 0.0),
                    'Minimap': False,
                    'Objects': {
                        '1210981190.74kmuller': {
                            'Type': 'LOD Sphere',
                            'Hpr': Point3(0.0, 0.0, 0.0),
                            'Pos': Point3(11.657, 10.594, 0.0),
                            'Radi': [100.0, 400.0, 1200.0],
                            'Scale': VBase3(1.0, 1.0, 1.0),
                            'VisSize': ''
                        }
                    },
                    'Pos': Point3(24676.654, 6182.396, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Undockable': True,
                    'VisSize': '',
                    'Visibility': 'Grid',
                    'Visual': {
                        'Model': 'models/islands/pir_m_are_isl_rockSmall'
                    }
                },
                '1210197632.0WDIG': {
                    'Type': 'Ship Spawn Node',
                    'Flagship': True,
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Level': '3',
                    'Pos': Point3(14231.835, 30915.141, 0.004),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'SKEL_SHADOW_CROW_FR',
                    'Team': 'default',
                    'Visual': {
                        'Color': (0, 0, 0.65, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1210197760.0WDIG': {
                    'Type': 'Ship Spawn Node',
                    'Flagship': True,
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Level': '3',
                    'Pos': Point3(26959.834, 31042.932, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'SKEL_HELLHOUND_FR',
                    'Team': 'default',
                    'Visual': {
                        'Color': (0, 0, 0.65, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1210197760.0WDIG0': {
                    'Type': 'Ship Spawn Node',
                    'Flagship': True,
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Level': '3',
                    'Pos': Point3(27378.008, 17669.408, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'SKEL_BLOOD_SCOURGE_FR',
                    'Team': 'default',
                    'Visual': {
                        'Color': (0, 0, 0.65, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1210197760.0WDIG1': {
                    'Type': 'Ship Spawn Node',
                    'Flagship': True,
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Level': '3',
                    'Pos': Point3(8032.644, -5340.035, 39.992),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'SKEL_SHADOW_CROW_SP',
                    'Team': 'default',
                    'Visual': {
                        'Color': (0, 0, 0.65, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1210197760.0WDIG2': {
                    'Type': 'Ship Spawn Node',
                    'Flagship': True,
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Level': '3',
                    'Pos': Point3(18731.025, -5261.008, -0.004),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'SKEL_HELLHOUND_SP',
                    'Team': 'default',
                    'Visual': {
                        'Color': (0, 0, 0.65, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1210197760.0WDIG3': {
                    'Type': 'Ship Spawn Node',
                    'Flagship': True,
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Level': '3',
                    'Pos': Point3(13163.561, -15632.86, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'SKEL_BLOOD_SCOURGE_SP',
                    'Team': 'default',
                    'Visual': {
                        'Color': (0, 0, 0.65, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1210197760.0WDIG4': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(24100.469, 29200.008, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1210197760.0WDIG5': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(24590.801, 20762.211, 39.988),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1210197888.0WDIG': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(18258.734, 20859.678, 39.992),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1210197888.0WDIG0': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(15509.665, -7156.37, 40.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1210197888.0WDIG1': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(15791.191, -12857.672, -0.012),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1210197888.0WDIG2': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(8795.961, -8645.371, 39.996),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1233100928.0akelts': {
                    'Type': 'Island',
                    'Name': 'Padres Del Fuego',
                    'File': 'DelFuegoIsland',
                    'Hpr': VBase3(-59.144, 0.0, 0.0),
                    'Objects': {
                        '1142029069.97sdnaik': {
                            'Type': 'LOD Sphere',
                            'Hpr': VBase3(96.557, 0.0, 0.0),
                            'Pos': Point3(-444.148, -440.057, 454.457),
                            'Radi': [2000.0, 2600.0, 6000.0],
                            'Scale': VBase3(1.0, 1.0, 1.0),
                            'VisSize': ''
                        }
                    },
                    'Phase': 1,
                    'Pos': Point3(8757.1, -24577.305, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Visual': {
                        'Model': 'models/islands/pir_m_are_isl_delFuego'
                    }
                },
                '1264194816.0kanpatel': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(17948.6, -11892.882, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0.0, 0.0, 1.0),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264194816.0kanpatel0': {
                    'Type': 'Ship Movement Node',
                    'Name': 'TF_KINGSHEAD_10',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(14286.487, -12852.007, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264194944.0kanpatel': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(8615.047, -12498.265, 40.008),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264194944.0kanpatel0': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-2018.253, -9970.679, 40.008),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264194944.0kanpatel1': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-5417.421, -7878.882, 40.008),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264194944.0kanpatel2': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-7247.745, -3869.609, 40.008),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264195072.0kanpatel': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-7509.217, 2057.153, 40.008),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264195072.0kanpatel0': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-6116.716, 7115.231, 0.008),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264195072.0kanpatel1': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-4111.274, 12085.251, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264195072.0kanpatel2': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-4721.626, 18014.387, 0.008),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264195072.0kanpatel3': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-7596.376, 22103.539, 40.008),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264195072.0kanpatel4': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-11954.285, 26199.977, 40.008),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264195200.0kanpatel0': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-20154.824, 29872.664, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264195968.0kanpatel': {
                    'Type': 'Ship Movement Node',
                    'Name': 'TF_PADRES',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(3910.5, -24099.93, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264196096.0kanpatel': {
                    'Type': 'Ship Movement Node',
                    'Name': 'TF_PADRES',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-100.775, -21911.348, 40.008),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264196096.0kanpatel0': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-4110.049, -17989.227, 40.008),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264196096.0kanpatel1': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-8032.167, -13979.952, 40.008),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264196096.0kanpatel2': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-10734.073, -9883.515, 40.008),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264196224.0kanpatel': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-12500.0, -4600.0, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264196224.0kanpatel0': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-11954.285, 836.938, 40.008),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264196224.0kanpatel1': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-12743.399, 6068.915, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264196224.0kanpatel2': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-15353.454, 9988.548, 40.008),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264196224.0kanpatel3': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-20000.0, 13500.0, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264196224.0kanpatel4': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-25376.643, 17048.363, 40.008),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264196352.0kanpatel': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-29048.529, 22025.273, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264196352.0kanpatel0': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-30000.0, 26000.0, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264196352.0kanpatel3': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-29658.879, 29959.852, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264196864.0kanpatel': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(29894.07, -4001.898, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264196864.0kanpatel0': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(24740.074, 14.989, 0.004),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264196864.0kanpatel1': {
                    'Type': 'Ship Movement Node',
                    'Name': 'TF_C',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(19952.059, 2101.175, 40.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264196992.0kanpatel0': {
                    'Type': 'Ship Movement Node',
                    'Name': 'TF_C',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(12159.232, 3342.153, 0.004),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264196992.0kanpatel1': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(5976.99, 4854.626, 40.004),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264196992.0kanpatel2': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(1189.987, 8644.823, 0.004),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264196992.0kanpatel3': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-776.762, 14829.401, 40.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264196992.0kanpatel4': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-1617.306, 20861.758, 0.004),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264196992.0kanpatel5': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-4216.654, 26216.41, 0.008),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264196992.0kanpatel6': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-7958.929, 29929.738, 0.004),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264197376.0kanpatel': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-27915.018, -21963.695, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264197376.0kanpatel0': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-19893.244, -19958.254, 0.008),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264197376.0kanpatel1': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-12569.015, -15947.366, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264197504.0kanpatel': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-8990.906, -10014.253, 40.008),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264197504.0kanpatel0': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-8000.0, -1500.0, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264197504.0kanpatel1': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-9252.385, 6022.852, 40.008),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264197504.0kanpatel2': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-6291.105, 12216.032, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264197632.0kanpatel': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-1000.0, 17500.0, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264197632.0kanpatel0': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(5913.142, 22147.117, 40.008),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264197632.0kanpatel1': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(10000.0, 30000.0, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264198016.0kanpatel': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-10036.806, -28143.156, 40.008),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264198016.0kanpatel0': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-3152.149, -24056.336, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264198016.0kanpatel1': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(2079.441, -17952.809, 0.008),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264198016.0kanpatel2': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(6000.299, -11931.737, 40.008),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264198016.0kanpatel3': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(10183.891, -3826.019, 40.008),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264198016.0kanpatel4': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(13931.692, 4105.375, 40.008),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264198144.0kanpatel0': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(15943.161, 12390.423, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264198144.0kanpatel1': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(20642.869, 19881.004, 40.008),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264198144.0kanpatel2': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(25883.184, 26602.914, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264198144.0kanpatel3': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(30068.457, 29916.262, -0.008),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264198272.0kanpatel': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-27991.391, -11931.74, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264198400.0kanpatel': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-21018.736, -8096.781, 40.008),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264198400.0kanpatel0': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-14743.349, -4000.343, 40.008),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264198400.0kanpatel1': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-10476.377, 1014.43, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264198400.0kanpatel2': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-10040.411, 6071.64, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264198400.0kanpatel3': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-12958.66, 10216.03, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264198400.0kanpatel4': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-12000.0, 16050.68, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264198400.0kanpatel5': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-7000.91, 22147.119, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264198400.0kanpatel6': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-1000.54, 27000.15, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1264198400.0kanpatel7': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(5218.399, 30003.445, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1156207188.828659a2': {
                    'Type': 'Island',
                    'File': 'antiguaIsland',
                    'Hpr': Point3(0.0 , 0.0, 0.0),
                    'Objects': {
                        '1157082007.828659a2': {
                            'Type': 'Imported Object',
                            'Hpr': Point3(0.0, 0.0, 0.0),
                            'Pos': Point3(0.0, 0.0, 0.0),
                            'Scale': VBase3(1.0, 1.0, 1.0),
                            'Visual': {
                                'Model': ['models/islands/pir_m_are_isl_antigua_idle']
                            }
                        }
                    },
                    'Undockable': True,
                    'Pos': Point3(-18670.057, 25398.319, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Visual': {
                        'Model': 'models/islands/pir_m_are_isl_antigua'
                    }
                },
                '1271348547.01akelts': {
                    'Type': 'Island',
                    'Name': "Raven's Cove",
                    'File': 'RavensCoveIsland',
                    'Environment': 'OpenSky',
                    'Hpr': VBase3(-45.724, 0.0, 0.0),
                    'Minimap': False,
                    'Objects': {
                        '1264624863.65caoconno': {
                            'Type': 'LOD Sphere',
                            'Hpr': VBase3(-89.652, 0.0, 0.0),
                            'Pos': Point3(0.0, 0.0, 0.0),
                            'Radi': [1300.0, 2000.0, 7000.0],
                            'Scale': VBase3(1.0, 1.0, 1.0),
                            'VisSize': ''
                        }
                    },
                    'Pos': Point3(-31670.057, 12398.319, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Undockable': False,
                    'VisSize': '',
                    'Visibility': 'Section',
                    'Visual': {
                        'Model': 'models/islands/pir_m_are_isl_ravensCove'
                    }
                },
                '1301961642.84jloehrle': {
                    'Type': 'Ship Movement Node',
                    'Hpr': VBase3(0.0, 0.0, 0.0),
                    'Pos': Point3(499.578, -18144.457, 39.994),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1301961658.36jloehrle': {
                    'Type': 'Ship Movement Node',
                    'Hpr': VBase3(0.0, 0.0, 0.0),
                    'Pos': Point3(-5394.646, -13968.187, 39.996),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1301961787.78jloehrle': {
                    'Type': 'Ship Movement Node',
                    'Hpr': VBase3(-45.724, 0.0, 0.0),
                    'Pos': Point3(-13357.119, -14372.964, 0.006),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1301961875.5jloehrle': {
                    'Type': 'Ship Movement Node',
                    'Hpr': VBase3(0.0, 0.0, 0.0),
                    'Pos': Point3(-19551.619, -15266.349, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1301961893.49jloehrle': {
                    'Type': 'Ship Movement Node',
                    'Hpr': VBase3(-45.724, 0.0, 0.0),
                    'Pos': Point3(-23662.166, -5910.755, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1301961921.19jloehrle': {
                    'Type': 'Ship Movement Node',
                    'Hpr': VBase3(-45.724, 0.0, 0.0),
                    'Pos': Point3(-10665.203, -4943.347, 40.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1301961947.74jloehrle': {
                    'Type': 'Ship Movement Node',
                    'Hpr': VBase3(0.0, 0.0, 0.0),
                    'Pos': Point3(538.598, -12235.405, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1302027202.34jloehrle': {
                    'Type': 'Ship Movement Node',
                    'Hpr': VBase3(0.0, 0.0, 0.0),
                    'Pos': Point3(14559.385, 11029.28, -0.004),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1302027210.82jloehrle': {
                    'Type': 'Ship Movement Node',
                    'Hpr': VBase3(0.0, 0.0, 0.0),
                    'Pos': Point3(5122.244, 12460.488, 39.996),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1302027247.31jloehrle': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(4148.283, 18201.814, -0.004),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1302027276.39jloehrle': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(7703.354, 24400.418, 39.992),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1302027297.28jloehrle': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(17793.635, 29823.191, -0.004),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1302027328.71jloehrle': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(25174.354, 28335.57, -0.004),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1302027345.21jloehrle': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(24028.979, 18421.74, -0.008),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1302027700.44jloehrle': {
                    'Type': 'Ship Movement Node',
                    'Hpr': VBase3(0.0, 0.0, 0.0),
                    'Pos': Point3(-24435.404, 3179.066, -0.008),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1302027714.3jloehrle': {
                    'Type': 'Ship Movement Node',
                    'Hpr': VBase3(0.0, 0.0, 0.0),
                    'Pos': Point3(-17657.785, 11250.238, -0.004),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1302027734.68jloehrle': {
                    'Type': 'Ship Movement Node',
                    'Hpr': VBase3(0.0, 0.0, 0.0),
                    'Pos': Point3(-12281.977, 19226.277, -0.012),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1302027809.08jloehrle': {
                    'Type': 'Ship Movement Node',
                    'Hpr': VBase3(0.0, 0.0, 0.0),
                    'Pos': Point3(-15691.225, 26470.641, -0.008),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1302027835.68jloehrle': {
                    'Type': 'Ship Movement Node',
                    'Hpr': VBase3(0.0, 0.0, 0.0),
                    'Pos': Point3(-25023.926, 27671.133, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1302027852.97jloehrle': {
                    'Type': 'Ship Movement Node',
                    'Hpr': VBase3(0.0, 0.0, 0.0),
                    'Pos': Point3(-28043.447, 19938.322, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1302027866.65jloehrle': {
                    'Type': 'Ship Movement Node',
                    'Hpr': VBase3(0.0, 0.0, 0.0),
                    'Pos': Point3(-24063.785, 12952.978, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1302027883.94jloehrle': {
                    'Type': 'Ship Movement Node',
                    'Hpr': VBase3(0.0, 0.0, 0.0),
                    'Pos': Point3(-25928.664, 7070.766, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                }
            }
        }
    },
    'Ocean Areas': [
        [Point3(11000, -1000, 0), Point3(-3000, 15000, 0), 'Windward_Passage', '1180566400.0dxschafe0'],
        [Point3(-29000, 21000, 0), Point3(-15000, 9000, 0), 'Brigand_Bay', '1180567552.0dxschafe'],
        [Point3(11000, 27000, 0), Point3(-3000, 21000, 0), 'Blackheart_Strait', '1180568320.0dxschafe'],
        [Point3(13000, 27000, 0), Point3(25000, 15000, 0), 'Salty_Flats', '1180569600.0dxschafe'],
        [Point3(25000, 13000, 0), Point3(13000, -1000, 0), 'Mar_de_Plata', '1180569728.0dxschafe0'],
        [Point3(17000, -3000, 0), Point3(3000, -15000, 0), 'Smugglers_Run', '1180570240.0dxschafe'],
        [Point3(19000, -9000, 0), Point3(21000, -15000, 0), 'Smugglers_Run', '1180570240.0dxschafe0'],
        [Point3(25000, -13000, 0), Point3(23000, -15000, 0), 'The_Hinterseas', '1180570368.0dxschafe'],
        [Point3(15000, -17000, 0), Point3(25000, -29000, 0), 'The_Hinterseas', '1180570368.0dxschafe0'],
        [Point3(25000, -11000, 0), Point3(23000, -9000, 0), 'Mar_de_Plata', '1180570496.0dxschafe'],
        [Point3(19000, -7000, 0), Point3(25000, -3000, 0), 'Mar_de_Plata', '1180570496.0dxschafe0'],
        [Point3(13000, -23000, 0), Point3(3000, -17000, 0), 'Boiling_Bay', '1180571008.0dxschafe'],
        [Point3(13000, -25000, 0), Point3(-15000, -29000, 0), 'Mariners_Reef', '1180571008.0dxschafe0'],
        [Point3(-3000, 19000, 0), Point3(3000, 17000, 0), 'Blackheart_Strait', '1180571264.0dxschafe'],
        [Point3(5000, 19000, 0), Point3(11000, 17000, 0), 'Windward_Passage', '1180571776.0dxschafe'],
        [Point3(-13000, 9000, 0), Point3(-5000, 27000, 0), 'Scurvy_Shallows', '1191538304.0dxschafe'],
        [Point3(-29000, -7000, 0), Point3(-13000, -15000, 0), 'Dead_Mans_Trough', '1191539072.0dxschafe0'],
        [Point3(-11000, -23000, 0), Point3(1000, -7000, 0), 'Leeward_Passage', '1191539328.0dxschafe'],
        [Point3(-15000, -17000, 0), Point3(-13000, -23000, 0), 'Leeward_Passage', '1191539328.0dxschafe0'],
        [Point3(-29000, 7000, 0), Point3(-5000, -5000, 0), 'Bloody_Bayou', '1191539328.0dxschafe1'],
        [Point3(-3000, -3000, 0), Point3(1000, -5000, 0), 'Bloody_Bayou', '1191539328.0dxschafe2']
    ],
    'Node Links': [
        ['1185235968.0dxschafe1', '1185235968.0dxschafe0', 'Bi-directional'],
        ['1185236224.0dxschafe', '1185236224.0dxschafe3', 'Bi-directional'],
        ['1185236480.0dxschafe', '1185236736.0dxschafe', 'Bi-directional'],
        ['1185236864.0dxschafe', '1185236480.0dxschafe1', 'Bi-directional'],
        ['1185237120.0dxschafe2', '1185237120.0dxschafe', 'Bi-directional'],
        ['1185237248.0dxschafe', '1185237120.0dxschafe1', 'Bi-directional'],
        ['1210197760.0WDIG4', '1210197632.0WDIG', 'Bi-directional'],
        ['1210197760.0WDIG5', '1210197760.0WDIG', 'Bi-directional'],
        ['1210197888.0WDIG', '1210197760.0WDIG0', 'Bi-directional'],
        ['1210197888.0WDIG0', '1210197760.0WDIG1', 'Bi-directional'],
        ['1210197760.0WDIG2', '1210197888.0WDIG1', 'Bi-directional'],
        ['1210197888.0WDIG2', '1210197760.0WDIG3', 'Bi-directional'],
        ['1264194816.0kanpatel', '1264194816.0kanpatel0', 'Direction 2'],
        ['1264194816.0kanpatel0', '1264194944.0kanpatel', 'Direction 2'],
        ['1264194944.0kanpatel', '1264194944.0kanpatel0', 'Direction 2'],
        ['1264194944.0kanpatel0', '1264194944.0kanpatel1', 'Direction 2'],
        ['1264194944.0kanpatel1', '1264194944.0kanpatel2', 'Direction 2'],
        ['1264194944.0kanpatel2', '1264195072.0kanpatel', 'Direction 2'],
        ['1264195072.0kanpatel', '1264195072.0kanpatel0', 'Direction 2'],
        ['1264195072.0kanpatel0', '1264195072.0kanpatel1', 'Direction 2'],
        ['1264195072.0kanpatel1', '1264195072.0kanpatel2', 'Direction 2'],
        ['1264195072.0kanpatel2', '1264195072.0kanpatel3', 'Direction 2'],
        ['1264195072.0kanpatel3', '1264195072.0kanpatel4', 'Direction 2'],
        ['1264195072.0kanpatel4', '1264195200.0kanpatel0', 'Direction 2'],
        ['1264195968.0kanpatel', '1264196096.0kanpatel', 'Direction 2'],
        ['1264196096.0kanpatel', '1264196096.0kanpatel0', 'Direction 2'],
        ['1264196096.0kanpatel0', '1264196096.0kanpatel1', 'Direction 2'],
        ['1264196096.0kanpatel1', '1264196096.0kanpatel2', 'Direction 2'],
        ['1264196096.0kanpatel2', '1264196224.0kanpatel', 'Direction 2'],
        ['1264196224.0kanpatel', '1264196224.0kanpatel0', 'Direction 2'],
        ['1264196224.0kanpatel0', '1264196224.0kanpatel1', 'Direction 2'],
        ['1264196224.0kanpatel1', '1264196224.0kanpatel2', 'Direction 2'],
        ['1264196224.0kanpatel2', '1264196224.0kanpatel3', 'Direction 2'],
        ['1264196224.0kanpatel3', '1264196224.0kanpatel4', 'Direction 2'],
        ['1264196224.0kanpatel4', '1264196352.0kanpatel', 'Direction 2'],
        ['1264196352.0kanpatel', '1264196352.0kanpatel0', 'Direction 2'],
        ['1264196352.0kanpatel0', '1264196352.0kanpatel3', 'Direction 2'],
        ['1264196864.0kanpatel', '1264196864.0kanpatel0', 'Direction 2'],
        ['1264196864.0kanpatel0', '1264196864.0kanpatel1', 'Direction 2'],
        ['1264196864.0kanpatel1', '1264196992.0kanpatel0', 'Direction 2'],
        ['1264196992.0kanpatel0', '1264196992.0kanpatel1', 'Direction 2'],
        ['1264196992.0kanpatel1', '1264196992.0kanpatel2', 'Direction 2'],
        ['1264196992.0kanpatel2', '1264196992.0kanpatel3', 'Direction 2'],
        ['1264196992.0kanpatel3', '1264196992.0kanpatel4', 'Direction 2'],
        ['1264196992.0kanpatel4', '1264196992.0kanpatel5', 'Direction 2'],
        ['1264196992.0kanpatel5', '1264196992.0kanpatel6', 'Direction 2'],
        ['1264197632.0kanpatel0', '1264197632.0kanpatel1', 'Direction 2'],
        ['1264197632.0kanpatel', '1264197632.0kanpatel0', 'Direction 2'],
        ['1264197504.0kanpatel2', '1264197632.0kanpatel', 'Direction 2'],
        ['1264197504.0kanpatel1', '1264197504.0kanpatel2', 'Direction 2'],
        ['1264197504.0kanpatel0', '1264197504.0kanpatel1', 'Direction 2'],
        ['1264197504.0kanpatel', '1264197504.0kanpatel0', 'Direction 2'],
        ['1264197376.0kanpatel1', '1264197504.0kanpatel', 'Direction 2'],
        ['1264197376.0kanpatel0', '1264197376.0kanpatel1', 'Direction 2'],
        ['1264197376.0kanpatel', '1264197376.0kanpatel0', 'Direction 2'],
        ['1264198016.0kanpatel', '1264198016.0kanpatel0', 'Direction 2'],
        ['1264198016.0kanpatel0', '1264198016.0kanpatel1', 'Direction 2'],
        ['1264198016.0kanpatel1', '1264198016.0kanpatel2', 'Direction 2'],
        ['1264198016.0kanpatel2', '1264198016.0kanpatel3', 'Direction 2'],
        ['1264198016.0kanpatel3', '1264198016.0kanpatel4', 'Direction 2'],
        ['1264198016.0kanpatel4', '1264198144.0kanpatel0', 'Direction 2'],
        ['1264198144.0kanpatel0', '1264198144.0kanpatel1', 'Direction 2'],
        ['1264198144.0kanpatel1', '1264198144.0kanpatel2', 'Direction 2'],
        ['1264198144.0kanpatel2', '1264198144.0kanpatel3', 'Direction 2'],
        ['1264198272.0kanpatel', '1264198400.0kanpatel', 'Direction 2'],
        ['1264198400.0kanpatel', '1264198400.0kanpatel0', 'Direction 2'],
        ['1264198400.0kanpatel0', '1264198400.0kanpatel1', 'Direction 2'],
        ['1264198400.0kanpatel1', '1264198400.0kanpatel2', 'Direction 2'],
        ['1264198400.0kanpatel2', '1264198400.0kanpatel3', 'Direction 2'],
        ['1264198400.0kanpatel3', '1264198400.0kanpatel4', 'Direction 2'],
        ['1264198400.0kanpatel4', '1264198400.0kanpatel5', 'Direction 2'],
        ['1264198400.0kanpatel5', '1264198400.0kanpatel6', 'Direction 2'],
        ['1264198400.0kanpatel6', '1264198400.0kanpatel7', 'Direction 2'],
        ['1301961642.84jloehrle', '1301961658.36jloehrle', 'Direction 2'],
        ['1301961658.36jloehrle', '1301961787.78jloehrle', 'Direction 2'],
        ['1301961787.78jloehrle', '1301961875.5jloehrle', 'Direction 2'],
        ['1301961875.5jloehrle', '1301961893.49jloehrle', 'Direction 2'],
        ['1301961893.49jloehrle', '1301961921.19jloehrle', 'Direction 2'],
        ['1301961921.19jloehrle', '1301961947.74jloehrle', 'Direction 2'],
        ['1301961642.84jloehrle', '1301961947.74jloehrle', 'Direction 1'],
        ['1302027202.34jloehrle', '1302027210.82jloehrle', 'Direction 2'],
        ['1302027210.82jloehrle', '1302027247.31jloehrle', 'Direction 2'],
        ['1302027247.31jloehrle', '1302027276.39jloehrle', 'Direction 2'],
        ['1302027276.39jloehrle', '1302027297.28jloehrle', 'Direction 2'],
        ['1302027297.28jloehrle', '1302027328.71jloehrle', 'Direction 2'],
        ['1302027328.71jloehrle', '1302027345.21jloehrle', 'Direction 2'],
        ['1302027202.34jloehrle', '1302027345.21jloehrle', 'Direction 1'],
        ['1302027700.44jloehrle', '1302027714.3jloehrle', 'Direction 2'],
        ['1302027714.3jloehrle', '1302027734.68jloehrle', 'Direction 2'],
        ['1302027734.68jloehrle', '1302027809.08jloehrle', 'Direction 2'],
        ['1302027809.08jloehrle', '1302027835.68jloehrle', 'Direction 2'],
        ['1302027835.68jloehrle', '1302027852.97jloehrle', 'Direction 2'],
        ['1302027852.97jloehrle', '1302027866.65jloehrle', 'Direction 2'],
        ['1302027866.65jloehrle', '1302027883.94jloehrle', 'Direction 2'],
        ['1302027700.44jloehrle', '1302027883.94jloehrle', 'Direction 1']
    ],
    'Layers': {
        'Collisions': ['1184008208.59kmuller', '1184016064.62kmuller', '1184013852.84kmuller', '1185822696.06kmuller', '1184006140.32kmuller', '1184002350.98kmuller', '1184007573.29kmuller', '1184021176.59kmuller', '1184005963.59kmuller', '1188324241.31akelts', '1184006537.34kmuller', '1184006605.81kmuller', '1187139568.33kmuller', '1188324186.98akelts', '1184006730.66kmuller', '1184007538.51kmuller', '1184006188.41kmuller', '1184021084.27kmuller', '1185824396.94kmuller', '1185824250.16kmuller', '1185823630.52kmuller', '1185823760.23kmuller', '1185824497.83kmuller', '1185824751.45kmuller', '1187739103.34akelts', '1188323993.34akelts', '1184016538.29kmuller', '1185822200.97kmuller', '1184016225.99kmuller', '1195241421.34akelts', '1195242796.08akelts', '1184020642.13kmuller', '1195237994.63akelts', '1184020756.88kmuller', '1184020833.4kmuller', '1185820992.97kmuller', '1185821053.83kmuller', '1184015068.54kmuller', '1184014935.82kmuller', '1185821432.88kmuller', '1185821701.86kmuller', '1195240137.55akelts', '1195241539.38akelts', '1195238422.3akelts', '1195238473.22akelts', '1185821453.17kmuller', '1184021269.96kmuller', '1185821310.89kmuller', '1185821165.59kmuller', '1185821199.36kmuller', '1185822035.98kmuller', '1184015806.59kmuller', '1185822059.48kmuller', '1185920461.76kmuller', '1194984449.66akelts', '1185824206.22kmuller', '1184003446.23kmuller', '1184003254.85kmuller', '1184003218.74kmuller', '1184002700.44kmuller', '1186705073.11kmuller', '1187658531.86akelts', '1186705214.3kmuller', '1185824927.28kmuller', '1184014204.54kmuller', '1184014152.84kmuller']
    },
    'ObjectIds': {
        '1141410776.53sdnaik': '["Objects"]["1141410776.53sdnaik"]',
        '1142029069.97sdnaik': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1233100928.0akelts"]["Objects"]["1142029069.97sdnaik"]',
        '1150922126.8dzlu': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1150922126.8dzlu"]',
        '1156207188.95dzlu': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1156207188.95dzlu"]',
        '1264624291.62caoconno': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264624291.62caoconno"]',
        '1150922126.828659a2': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1150922126.828659a2"]',
        '1156207188.828659a2': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1156207188.828659a2"]',
        '1156359855.24bbathen': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1156359855.24bbathen"]',
        '1157060429.94sdnaik': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1150922126.8dzlu"]["Objects"]["1157060429.94sdnaik"]',
        '1158214327.11sdnaik': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1156207188.95dzlu"]["Objects"]["1158214327.11sdnaik"]',
        '1158296490.13sdnaik': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1156359855.24bbathen"]["Objects"]["1158296490.13sdnaik"]',
        '1159933206.48sdnaik': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1159933206.48sdnaik"]',
        '1160614528.73sdnaik': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1160614528.73sdnaik"]',
        '1161282725.84kmuller': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1161282725.84kmuller"]',
        '1161664293.39sdnaik': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1161282725.84kmuller"]["Objects"]["1161664293.39sdnaik"]',
        '1162600600.5sdnaik': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1159933206.48sdnaik"]["Objects"]["1162600600.5sdnaik"]',
        '1163119750.53sdnaik': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1160614528.73sdnaik"]["Objects"]["1163119750.53sdnaik"]',
        '1164135492.81dzlu': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1164135492.81dzlu"]',
        '1164150392.42dzlu': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1164150392.42dzlu"]',
        '1164157132.99dzlu': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1164157132.99dzlu"]',
        '1164760526.77sdnaik': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1173381952.2sdnaik"]["Objects"]["1164760526.77sdnaik"]',
        '1164760719.72sdnaik': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1164135492.81dzlu"]["Objects"]["1164760719.72sdnaik"]',
        '1164763706.66sdnaik': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1164763706.66sdnaik"]',
        '1164763735.42sdnaik': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1164763706.66sdnaik"]["Objects"]["1164763735.42sdnaik"]',
        '1164763977.22sdnaik': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1164157132.99dzlu"]["Objects"]["1164763977.22sdnaik"]',
        '1173381952.2sdnaik': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1173381952.2sdnaik"]',
        '1173381974.5sdnaik': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1164150392.42dzlu"]["Objects"]["1173381974.5sdnaik"]',
        '1173382404.64sdnaik': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1173382404.64sdnaik"]',
        '1173382432.38sdnaik': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1173382404.64sdnaik"]["Objects"]["1173382432.38sdnaik"]',
        '1185235968.0dxschafe0': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1185235968.0dxschafe0"]',
        '1185235968.0dxschafe1': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1185235968.0dxschafe1"]',
        '1185236224.0dxschafe': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1185236224.0dxschafe"]',
        '1185236224.0dxschafe3': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1185236224.0dxschafe3"]',
        '1185236480.0dxschafe': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1185236480.0dxschafe"]',
        '1185236480.0dxschafe1': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1185236480.0dxschafe1"]',
        '1185236736.0dxschafe': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1185236736.0dxschafe"]',
        '1185236864.0dxschafe': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1185236864.0dxschafe"]',
        '1185237120.0dxschafe': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1185237120.0dxschafe"]',
        '1185237120.0dxschafe1': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1185237120.0dxschafe1"]',
        '1185237120.0dxschafe2': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1185237120.0dxschafe2"]',
        '1185237248.0dxschafe': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1185237248.0dxschafe"]',
        '1196970035.53sdnaik': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1196970035.53sdnaik"]',
        '1196970080.56sdnaik': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1196970080.56sdnaik"]',
        '1196970432.69sdnaik': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1196970035.53sdnaik"]["Objects"]["1196970432.69sdnaik"]',
        '1196970440.66sdnaik': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1196970080.56sdnaik"]["Objects"]["1196970440.66sdnaik"]',
        '1201636857.8kmuller': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1201636857.8kmuller"]',
        '1201641372.09kmuller': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1201641372.09kmuller"]',
        '1201641393.2kmuller': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1201641393.2kmuller"]',
        '1201641405.3kmuller': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1201641405.3kmuller"]',
        '1201641438.69kmuller': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1201641438.69kmuller"]',
        '1201641487.41kmuller': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1201641487.41kmuller"]',
        '1210197632.0WDIG': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1210197632.0WDIG"]',
        '1210197760.0WDIG': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1210197760.0WDIG"]',
        '1210197760.0WDIG0': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1210197760.0WDIG0"]',
        '1210197760.0WDIG1': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1210197760.0WDIG1"]',
        '1210197760.0WDIG2': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1210197760.0WDIG2"]',
        '1210197760.0WDIG3': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1210197760.0WDIG3"]',
        '1210197760.0WDIG4': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1210197760.0WDIG4"]',
        '1210197760.0WDIG5': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1210197760.0WDIG5"]',
        '1210197888.0WDIG': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1210197888.0WDIG"]',
        '1210197888.0WDIG0': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1210197888.0WDIG0"]',
        '1210197888.0WDIG1': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1210197888.0WDIG1"]',
        '1210197888.0WDIG2': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1210197888.0WDIG2"]',
        '1210981042.09kmuller': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1201636857.8kmuller"]["Objects"]["1210981042.09kmuller"]',
        '1210981113.03kmuller': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1201641372.09kmuller"]["Objects"]["1210981113.03kmuller"]',
        '1210981144.78kmuller': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1201641393.2kmuller"]["Objects"]["1210981144.78kmuller"]',
        '1210981190.74kmuller': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1201641487.41kmuller"]["Objects"]["1210981190.74kmuller"]',
        '1210981205.23kmuller': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1201641405.3kmuller"]["Objects"]["1210981205.23kmuller"]',
        '1210981266.57kmuller': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1201641438.69kmuller"]["Objects"]["1210981266.57kmuller"]',
        '1233100928.0akelts': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1233100928.0akelts"]',
        '1264194816.0kanpatel': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264194816.0kanpatel"]',
        '1264194816.0kanpatel0': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264194816.0kanpatel0"]',
        '1264194944.0kanpatel': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264194944.0kanpatel"]',
        '1264194944.0kanpatel0': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264194944.0kanpatel0"]',
        '1264194944.0kanpatel1': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264194944.0kanpatel1"]',
        '1264194944.0kanpatel2': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264194944.0kanpatel2"]',
        '1264195072.0kanpatel': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264195072.0kanpatel"]',
        '1264195072.0kanpatel0': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264195072.0kanpatel0"]',
        '1264195072.0kanpatel1': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264195072.0kanpatel1"]',
        '1264195072.0kanpatel2': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264195072.0kanpatel2"]',
        '1264195072.0kanpatel3': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264195072.0kanpatel3"]',
        '1264195072.0kanpatel4': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264195072.0kanpatel4"]',
        '1264195200.0kanpatel0': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264195200.0kanpatel0"]',
        '1264195968.0kanpatel': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264195968.0kanpatel"]',
        '1264196096.0kanpatel': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264196096.0kanpatel"]',
        '1264196096.0kanpatel0': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264196096.0kanpatel0"]',
        '1264196096.0kanpatel1': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264196096.0kanpatel1"]',
        '1264196096.0kanpatel2': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264196096.0kanpatel2"]',
        '1264196224.0kanpatel': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264196224.0kanpatel"]',
        '1264196224.0kanpatel0': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264196224.0kanpatel0"]',
        '1264196224.0kanpatel1': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264196224.0kanpatel1"]',
        '1264196224.0kanpatel2': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264196224.0kanpatel2"]',
        '1264196224.0kanpatel3': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264196224.0kanpatel3"]',
        '1264196224.0kanpatel4': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264196224.0kanpatel4"]',
        '1264196352.0kanpatel': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264196352.0kanpatel"]',
        '1264196352.0kanpatel0': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264196352.0kanpatel0"]',
        '1264196352.0kanpatel3': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264196352.0kanpatel3"]',
        '1264196864.0kanpatel': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264196864.0kanpatel"]',
        '1264196864.0kanpatel0': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264196864.0kanpatel0"]',
        '1264196864.0kanpatel1': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264196864.0kanpatel1"]',
        '1264196992.0kanpatel0': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264196992.0kanpatel0"]',
        '1264196992.0kanpatel1': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264196992.0kanpatel1"]',
        '1264196992.0kanpatel2': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264196992.0kanpatel2"]',
        '1264196992.0kanpatel3': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264196992.0kanpatel3"]',
        '1264196992.0kanpatel4': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264196992.0kanpatel4"]',
        '1264196992.0kanpatel5': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264196992.0kanpatel5"]',
        '1264196992.0kanpatel6': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264196992.0kanpatel6"]',
        '1264197376.0kanpatel': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264197376.0kanpatel"]',
        '1264197376.0kanpatel0': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264197376.0kanpatel0"]',
        '1264197376.0kanpatel1': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264197376.0kanpatel1"]',
        '1264197504.0kanpatel': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264197504.0kanpatel"]',
        '1264197504.0kanpatel0': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264197504.0kanpatel0"]',
        '1264197504.0kanpatel1': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264197504.0kanpatel1"]',
        '1264197504.0kanpatel2': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264197504.0kanpatel2"]',
        '1264197632.0kanpatel': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264197632.0kanpatel"]',
        '1264197632.0kanpatel0': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264197632.0kanpatel0"]',
        '1264197632.0kanpatel1': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264197632.0kanpatel1"]',
        '1264198016.0kanpatel': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264198016.0kanpatel"]',
        '1264198016.0kanpatel0': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264198016.0kanpatel0"]',
        '1264198016.0kanpatel1': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264198016.0kanpatel1"]',
        '1264198016.0kanpatel2': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264198016.0kanpatel2"]',
        '1264198016.0kanpatel3': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264198016.0kanpatel3"]',
        '1264198016.0kanpatel4': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264198016.0kanpatel4"]',
        '1264198144.0kanpatel0': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264198144.0kanpatel0"]',
        '1264198144.0kanpatel1': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264198144.0kanpatel1"]',
        '1264198144.0kanpatel2': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264198144.0kanpatel2"]',
        '1264198144.0kanpatel3': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264198144.0kanpatel3"]',
        '1264198272.0kanpatel': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264198272.0kanpatel"]',
        '1264198400.0kanpatel': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264198400.0kanpatel"]',
        '1264198400.0kanpatel0': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264198400.0kanpatel0"]',
        '1264198400.0kanpatel1': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264198400.0kanpatel1"]',
        '1264198400.0kanpatel2': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264198400.0kanpatel2"]',
        '1264198400.0kanpatel3': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264198400.0kanpatel3"]',
        '1264198400.0kanpatel4': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264198400.0kanpatel4"]',
        '1264198400.0kanpatel5': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264198400.0kanpatel5"]',
        '1264198400.0kanpatel6': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264198400.0kanpatel6"]',
        '1264198400.0kanpatel7': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1264198400.0kanpatel7"]',
        '1264624863.65caoconno': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1271348547.01akelts"]["Objects"]["1264624863.65caoconno"]',
        '1271348547.01akelts': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1271348547.01akelts"]',
        '1301961642.84jloehrle': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1301961642.84jloehrle"]',
        '1301961658.36jloehrle': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1301961658.36jloehrle"]',
        '1301961787.78jloehrle': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1301961787.78jloehrle"]',
        '1301961875.5jloehrle': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1301961875.5jloehrle"]',
        '1301961893.49jloehrle': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1301961893.49jloehrle"]',
        '1301961921.19jloehrle': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1301961921.19jloehrle"]',
        '1301961947.74jloehrle': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1301961947.74jloehrle"]',
        '1302027202.34jloehrle': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1302027202.34jloehrle"]',
        '1302027210.82jloehrle': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1302027210.82jloehrle"]',
        '1302027247.31jloehrle': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1302027247.31jloehrle"]',
        '1302027276.39jloehrle': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1302027276.39jloehrle"]',
        '1302027297.28jloehrle': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1302027297.28jloehrle"]',
        '1302027328.71jloehrle': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1302027328.71jloehrle"]',
        '1302027345.21jloehrle': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1302027345.21jloehrle"]',
        '1302027700.44jloehrle': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1302027700.44jloehrle"]',
        '1302027714.3jloehrle': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1302027714.3jloehrle"]',
        '1302027734.68jloehrle': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1302027734.68jloehrle"]',
        '1302027809.08jloehrle': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1302027809.08jloehrle"]',
        '1302027835.68jloehrle': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1302027835.68jloehrle"]',
        '1302027852.97jloehrle': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1302027852.97jloehrle"]',
        '1302027866.65jloehrle': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1302027866.65jloehrle"]',
        '1302027883.94jloehrle': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1302027883.94jloehrle"]'
    }
}
extraInfo = {
    'camPos': Point3(-33114.7, -40175.2, 54648.8),
    'camHpr': VBase3(-11.9216, -46.9344, 0),
    'focalLength': 1.39999997616,
    'skyState': 2,
    'fog': 0,
    'cameraSettings': {
        'overhead': {
            'camPos': Point3(-1059.51, -121.796, 99609.5),
            'camHpr': VBase3(0, -90, 0),
            'focalLength': 1.39999997616
        }
    }
}