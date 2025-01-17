import c4d

from ..Const import Const
from .JsonFunction import JsonFunction

const = Const()


class ConfigManagerRedshift(JsonFunction):
    def createRedshiftCheckBox(self, dialog):
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_ENABLE_VIEWPORT, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Viewport Enable")
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_ENABLE_RENDER, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Render Enable")
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_LIGHT_TYPE, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "LightType")
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_PREVIEW, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Preview")
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_SHOW_ILLUM, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Show Illum")
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_AFFECT_DIFFUSE, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Affects Diffuse")
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_AFFECT_SPECULAR, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Affects Specular")
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_COLORMODE, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Color Mode")
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_COLOR, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Color")
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_TEMP, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Temperature")
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_UNIT, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Unit")
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_LUMEN, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Luminous")
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_INTENSITY, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Light Intensity")
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_DECAY_TYPE, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Decay Type")
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_AREA_GEO, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Area Type")
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_AREA_SIZEX, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Area Size X")
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_AREA_SIZEY, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Area Size Y")
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_AREA_SIZEZ, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Area Size Z")
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_AREA_VISIBLE_RENDER, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Area Visible in Render")
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_AREA_BIDIRECTIONAL, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Area Bidirectional")
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_AREA_NORMALIZE, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Area Normalize")
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_AREA_SAMPLES, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Area Sample")
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_SPOT_ANGLE, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Spot Angle")
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_SPOT_FALLOFF, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Spot Faloff Angle")
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_DOME_ENVTYPE, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Dome Type")
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_DOME_APPLYEXPOSURECOMPENSATION, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Dome Camera Exposure compensation")
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_DOME_EXPOSURE, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Dome Exposure")
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_DOME_HUE, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Dome Hue")
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_DOME_SATURATION, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "DOME Saturation")
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_DOME_TINT, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Dome Tint")
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_DOME_SAMPLE, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Dome Sample")
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_IES_COLORMODE, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "IES Color Mode")
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_IES_COLOR, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "IES Color")
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_IES_TEMP, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "IES Temperature")
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_IES_MULT, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "IES Mult")
        dialog.AddCheckbox(const.REDSHIFT_OPTIONS_LIGHT_PORTAL_SIZEX, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Portal Size X")
        dialog.AddCheckbox(const.REDSHIFT_OPTIONS_LIGHT_PORTAL_SIZEY, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Portal Size Y")
        dialog.AddCheckbox(const.REDSHIFT_OPTIONS_LIGHT_PORTAL_MULTIPLIER, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Portal Mult")
        dialog.AddCheckbox(const.REDSHIFT_OPTIONS_LIGHT_PORTAL_TINT_COLOR, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Portal Tint")
        dialog.AddCheckbox(const.REDSHIFT_OPTIONS_LIGHT_PORTAL_TRANSPARENCY, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Portal Transparency")
        dialog.AddCheckbox(const.REDSHIFT_OPTIONS_LIGHT_PORTAL_SAMPLES, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Portal Samples")
        dialog.AddCheckbox(const.REDSHIFT_OPTIONS_LIGHT_PHYSICALSUN_MULTIPLIER, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Sky Intensity")
        dialog.AddCheckbox(const.REDSHIFT_OPTIONS_LIGHT_PHYSICALSUN_USENONPHYSICALINTENSITY, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Sky Non Physical")
        dialog.AddCheckbox(const.REDSHIFT_OPTIONS_LIGHT_PHYSICALSUN_SUN_DISK_SCALE, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Sky Disk Scale")
        dialog.AddCheckbox(const.REDSHIFT_OPTIONS_LIGHT_PHYSICALSUN_HAZE, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Sky Haze")
        dialog.AddCheckbox(const.REDSHIFT_OPTIONS_LIGHT_PHYSICALSUN_OZONE, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Sky Ozone")
        dialog.AddCheckbox(const.REDSHIFT_OPTIONS_LIGHT_PHYSICALSUN_HORIZON_HEIGHT, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Sky Height")
        dialog.AddCheckbox(const.REDSHIFT_OPTIONS_LIGHT_PHYSICALSUN_REDBLUESHIFT, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Sky Red-blueshift")
        dialog.AddCheckbox(const.REDSHIFT_OPTIONS_LIGHT_PHYSICALSUN_SATURATION, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Sky Saturation")
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_VOLUME, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Volume Contribution")
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_VOLUME_SAMPLE, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Volume Sample")
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_SHADOW_ENABLE, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Enable Shadow")
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_SHADOW_TRANPS, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Shadow Transparecy")
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_SHADOW_SOFTNESS, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Shadow Softness")
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_SHADOW_SAMPLE, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Shadow Sample")
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_PHOTON_ENABLED, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Caustics")
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_PHOTON_INTENSITY, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Caustics Mult")
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_PHOTON_NUM, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Caustic Num")
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_GI_ENABLED, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "GI")
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_GI_MULITPLIER, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "GI Mult")
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_GI_PHOTONS, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "GI Num")
        dialog.AddCheckbox(const.LIGHT_LISTER_REDSHIFT_OPTIONS_LAYERS, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "Layers")
        dialog.AddCheckbox(const.REDSHIFT_LIGHT_LIGHT_GROUP, c4d.BFH_LEFT | c4d.BFV_TOP, 0, 0, "AOV Light Groups")

        self.fillRedshiftCheckBox(dialog)

    def fillRedshiftCheckBox(self, dialog):
        self.jsonContent = self.loadJsonFile()
        self.redshiftConfig = self.jsonContent["redshift"]

        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_ENABLE_VIEWPORT, self.redshiftConfig["visibilityviewport"])
        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_ENABLE_RENDER, self.redshiftConfig["Visibilityrender"])
        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_LIGHT_TYPE, self.redshiftConfig["LightType"])
        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_PREVIEW, self.redshiftConfig["Preview"])
        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_SHOW_ILLUM, self.redshiftConfig["ShowIllum"])
        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_AFFECT_DIFFUSE, self.redshiftConfig["AffectsDiffuse"])
        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_AFFECT_SPECULAR, self.redshiftConfig["AffectsSpecular"])
        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_COLORMODE, self.redshiftConfig["Colormode"])
        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_COLOR, self.redshiftConfig["Color"])
        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_TEMP, self.redshiftConfig["Temperature"])
        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_UNIT, self.redshiftConfig["Unit"])
        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_LUMEN, self.redshiftConfig["Luminous"])
        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_INTENSITY, self.redshiftConfig["LightIntensity"])
        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_DECAY_TYPE, self.redshiftConfig["DecayType"])
        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_AREA_GEO, self.redshiftConfig["AreaType"])
        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_AREA_SIZEX, self.redshiftConfig["AREASizeX"])
        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_AREA_SIZEY, self.redshiftConfig["AREASizeY"])
        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_AREA_SIZEZ, self.redshiftConfig["AREASizeZ"])
        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_AREA_VISIBLE_RENDER, self.redshiftConfig["AREAVisibleinRender"])
        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_AREA_BIDIRECTIONAL, self.redshiftConfig["AREABidirectional"])
        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_AREA_NORMALIZE, self.redshiftConfig["AREANormalize"])
        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_AREA_SAMPLES, self.redshiftConfig["AREASample"])
        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_SPOT_ANGLE, self.redshiftConfig["SPOTAngle"])
        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_SPOT_FALLOFF, self.redshiftConfig["SPOTFaloffangle"])
        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_DOME_ENVTYPE, self.redshiftConfig["DomeType"])
        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_DOME_APPLYEXPOSURECOMPENSATION, self.redshiftConfig["DOMECompensateSRGB"])
        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_DOME_EXPOSURE, self.redshiftConfig["DOMEExposure"])
        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_DOME_HUE, self.redshiftConfig["DOMEHue"])
        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_DOME_SATURATION, self.redshiftConfig["DOMESaturation"])
        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_DOME_TINT, self.redshiftConfig["DOMETint"])
        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_DOME_SAMPLE, self.redshiftConfig["DOMESample"])
        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_IES_COLORMODE, self.redshiftConfig["IESColormode"])
        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_IES_COLOR, self.redshiftConfig["IESColor"])
        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_IES_TEMP, self.redshiftConfig["IESTemperature"])
        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_IES_MULT, self.redshiftConfig["IESmult"])
        dialog.SetBool(const.REDSHIFT_OPTIONS_LIGHT_PORTAL_SIZEX, self.redshiftConfig["PORTALsizeX"])
        dialog.SetBool(const.REDSHIFT_OPTIONS_LIGHT_PORTAL_SIZEY, self.redshiftConfig["PORTALsizeY"])
        dialog.SetBool(const.REDSHIFT_OPTIONS_LIGHT_PORTAL_MULTIPLIER, self.redshiftConfig["PORTALmult"])
        dialog.SetBool(const.REDSHIFT_OPTIONS_LIGHT_PORTAL_TINT_COLOR, self.redshiftConfig["PORTALtint"])
        dialog.SetBool(const.REDSHIFT_OPTIONS_LIGHT_PORTAL_TRANSPARENCY, self.redshiftConfig["PORTALTransparency"])
        dialog.SetBool(const.REDSHIFT_OPTIONS_LIGHT_PORTAL_SAMPLES, self.redshiftConfig["PORTALsamples"])
        dialog.SetBool(const.REDSHIFT_OPTIONS_LIGHT_PHYSICALSUN_MULTIPLIER, self.redshiftConfig["SKYIntensity"])
        dialog.SetBool(const.REDSHIFT_OPTIONS_LIGHT_PHYSICALSUN_USENONPHYSICALINTENSITY, self.redshiftConfig["SKYNonPhysical"])
        dialog.SetBool(const.REDSHIFT_OPTIONS_LIGHT_PHYSICALSUN_SUN_DISK_SCALE, self.redshiftConfig["SKYDiskScale"])
        dialog.SetBool(const.REDSHIFT_OPTIONS_LIGHT_PHYSICALSUN_HAZE, self.redshiftConfig["SKYHaze"])
        dialog.SetBool(const.REDSHIFT_OPTIONS_LIGHT_PHYSICALSUN_OZONE, self.redshiftConfig["SKYOzone"])
        dialog.SetBool(const.REDSHIFT_OPTIONS_LIGHT_PHYSICALSUN_HORIZON_HEIGHT, self.redshiftConfig["SKYHeight"])
        dialog.SetBool(const.REDSHIFT_OPTIONS_LIGHT_PHYSICALSUN_REDBLUESHIFT, self.redshiftConfig["SKYRed-blueshift"])
        dialog.SetBool(const.REDSHIFT_OPTIONS_LIGHT_PHYSICALSUN_SATURATION, self.redshiftConfig["SKYsaturation"])
        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_VOLUME, self.redshiftConfig["VolContribution"])
        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_VOLUME_SAMPLE, self.redshiftConfig["VolSample"])
        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_SHADOW_ENABLE, self.redshiftConfig["EnableShadow"])
        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_SHADOW_TRANPS, self.redshiftConfig["ShadowTransparecy"])
        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_SHADOW_SOFTNESS, self.redshiftConfig["ShadowSoftness"])
        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_SHADOW_SAMPLE, self.redshiftConfig["ShadowSample"])
        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_PHOTON_ENABLED, self.redshiftConfig["Caustics"])
        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_PHOTON_INTENSITY, self.redshiftConfig["Causticsmult"])
        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_PHOTON_NUM, self.redshiftConfig["Causticnum"])
        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_GI_ENABLED, self.redshiftConfig["GI"])
        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_GI_MULITPLIER, self.redshiftConfig["GImult"])
        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_GI_PHOTONS, self.redshiftConfig["GInum"])
        dialog.SetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_LAYERS, self.redshiftConfig["Layers"])
        dialog.SetBool(const.REDSHIFT_LIGHT_LIGHT_GROUP, self.redshiftConfig["LightGroup"])

    def generateRedshiftjson(self, dialog):
        redshift = {}
        redshift["visibilityviewport"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_ENABLE_VIEWPORT)
        redshift["Visibilityrender"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_ENABLE_RENDER)
        redshift["LightType"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_LIGHT_TYPE)
        redshift["Preview"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_PREVIEW)
        redshift["ShowIllum"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_SHOW_ILLUM)
        redshift["AffectsDiffuse"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_AFFECT_DIFFUSE)
        redshift["AffectsSpecular"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_AFFECT_SPECULAR)
        redshift["Colormode"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_COLORMODE)
        redshift["Color"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_COLOR)
        redshift["Temperature"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_TEMP)
        redshift["Unit"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_UNIT)
        redshift["Luminous"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_LUMEN)
        redshift["LightIntensity"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_INTENSITY)
        redshift["DecayType"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_DECAY_TYPE)
        redshift["AreaType"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_AREA_GEO)
        redshift["AREASizeX"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_AREA_SIZEX)
        redshift["AREASizeY"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_AREA_SIZEY)
        redshift["AREASizeZ"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_AREA_SIZEZ)
        redshift["AREAVisibleinRender"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_AREA_VISIBLE_RENDER)
        redshift["AREABidirectional"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_AREA_BIDIRECTIONAL)
        redshift["AREANormalize"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_AREA_NORMALIZE)
        redshift["AREASample"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_AREA_SAMPLES)
        redshift["SPOTAngle"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_SPOT_ANGLE)
        redshift["SPOTFaloffangle"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_SPOT_FALLOFF)
        redshift["DomeType"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_DOME_ENVTYPE)
        redshift["DOMECompensateSRGB"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_DOME_APPLYEXPOSURECOMPENSATION)
        redshift["DOMEExposure"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_DOME_EXPOSURE)
        redshift["DOMEHue"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_DOME_HUE)
        redshift["DOMESaturation"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_DOME_SATURATION)
        redshift["DOMETint"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_DOME_TINT)
        redshift["DOMESample"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_DOME_SAMPLE)
        redshift["IESColormode"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_IES_COLORMODE)
        redshift["IESColor"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_IES_COLOR)
        redshift["IESTemperature"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_IES_TEMP)
        redshift["IESmult"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_IES_MULT)
        redshift["PORTALsizeX"] = dialog.GetBool(const.REDSHIFT_OPTIONS_LIGHT_PORTAL_SIZEX)
        redshift["PORTALsizeY"] = dialog.GetBool(const.REDSHIFT_OPTIONS_LIGHT_PORTAL_SIZEY)
        redshift["PORTALmult"] = dialog.GetBool(const.REDSHIFT_OPTIONS_LIGHT_PORTAL_MULTIPLIER)
        redshift["PORTALtint"] = dialog.GetBool(const.REDSHIFT_OPTIONS_LIGHT_PORTAL_TINT_COLOR)
        redshift["PORTALTransparency"] = dialog.GetBool(const.REDSHIFT_OPTIONS_LIGHT_PORTAL_TRANSPARENCY)
        redshift["PORTALsamples"] = dialog.GetBool(const.REDSHIFT_OPTIONS_LIGHT_PORTAL_SAMPLES)
        redshift["SKYIntensity"] = dialog.GetBool(const.REDSHIFT_OPTIONS_LIGHT_PHYSICALSUN_MULTIPLIER)
        redshift["SKYNonPhysical"] = dialog.GetBool(const.REDSHIFT_OPTIONS_LIGHT_PHYSICALSUN_USENONPHYSICALINTENSITY)
        redshift["SKYDiskScale"] = dialog.GetBool(const.REDSHIFT_OPTIONS_LIGHT_PHYSICALSUN_SUN_DISK_SCALE)
        redshift["SKYHaze"] = dialog.GetBool(const.REDSHIFT_OPTIONS_LIGHT_PHYSICALSUN_HAZE)
        redshift["SKYOzone"] = dialog.GetBool(const.REDSHIFT_OPTIONS_LIGHT_PHYSICALSUN_OZONE)
        redshift["SKYHeight"] = dialog.GetBool(const.REDSHIFT_OPTIONS_LIGHT_PHYSICALSUN_HORIZON_HEIGHT)
        redshift["SKYRed-blueshift"] = dialog.GetBool(const.REDSHIFT_OPTIONS_LIGHT_PHYSICALSUN_REDBLUESHIFT)
        redshift["SKYsaturation"] = dialog.GetBool(const.REDSHIFT_OPTIONS_LIGHT_PHYSICALSUN_SATURATION)
        redshift["VolContribution"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_VOLUME)
        redshift["VolSample"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_VOLUME_SAMPLE)
        redshift["EnableShadow"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_SHADOW_ENABLE)
        redshift["ShadowTransparecy"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_SHADOW_TRANPS)
        redshift["ShadowSoftness"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_SHADOW_SOFTNESS)
        redshift["ShadowSample"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_SHADOW_SAMPLE)
        redshift["Caustics"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_PHOTON_ENABLED)
        redshift["Causticsmult"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_PHOTON_INTENSITY)
        redshift["Causticnum"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_PHOTON_NUM)
        redshift["GI"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_GI_ENABLED)
        redshift["GImult"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_GI_MULITPLIER)
        redshift["GInum"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_GI_PHOTONS)
        redshift["LightGroup"] = dialog.GetBool(const.REDSHIFT_LIGHT_LIGHT_GROUP)
        redshift["Layers"] = dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_OPTIONS_LAYERS)


        self.jsonContent["redshift"] = redshift