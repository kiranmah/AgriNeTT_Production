from django.contrib.gis.db import models

#Roads Model
class Roads(models.Model):
	objectID = models.IntegerField()
	fnode = models.IntegerField()
	tnode = models.IntegerField()
	length = models.IntegerField()
	streetgis = models.CharField(max_length=150)
	source = models.CharField(max_length=100)
	geomData = models.MultiLineStringField()
	objects = models.GeoManager()

class landParcel(models.Model):
    parcelno = models.CharField(max_length=20)
    parcelowne = models.CharField(max_length=80)
    area_acre = models.CharField(max_length=25)
    area_sf = models.CharField(max_length=25)
    area_sm = models.CharField(max_length=25)
    area_ha = models.CharField(max_length=25)
    landuseno = models.FloatField()
    landusetyp = models.CharField(max_length=25)
    planno = models.CharField(max_length=25)
    landbookid = models.CharField(max_length=30)
    errorno = models.FloatField()
    sheetno = models.CharField(max_length=25)
    mapscale = models.FloatField()
    geom = models.MultiPolygonField()
    objects = models.GeoManager()

class soilFeatures(models.Model):
    domsoil = models.CharField(max_length=25,unique=True)
    sand_prop = models.CharField(max_length=30)
    silt_prop = models.CharField(max_length=30)
    clay_prop = models.CharField(max_length=30)
    horizon_to_dept = models.FloatField(default = 0.0)
    phhorizon1 = models.CharField(max_length=30)
    ca = models.CharField(max_length=30)
    mg = models.CharField(max_length=30)
    k = models.CharField(max_length=30)
    na = models.CharField(max_length=30)
    cec = models.CharField(max_length=30)
    SoilSeriesName = models.CharField(max_length=80, null=True)
    SoilOrderName = models.CharField(max_length=80, null=True)
    exch_cations = models.CharField(max_length=30,default=None)
    c = models.CharField(max_length=30)
    n = models.CharField(max_length=30)
    freecaco3 = models.CharField(max_length=30)
    fertility = models.CharField(max_length=30)
    objects = models.GeoManager()

class landUse(models.Model):
    area = models.FloatField()
    perimeter = models.FloatField()
    landuse_field = models.FloatField()
    landuse_id = models.FloatField()
    classifaca = models.CharField(max_length=100)
    symbols_field = models.CharField(max_length=30)
    geomData = models.MultiPolygonField()
    objects = models.GeoManager()

#Soils Model
class Soils(models.Model):
	soilID = models.CharField(max_length=150,default=None)
	soilCode = models.CharField(max_length=25)
	soilName = models.CharField(max_length=150)
	soilLabel = models.CharField(max_length=150)
	tobacco = models.CharField(max_length=25)
	pasture = models.CharField(max_length=25)
	food_plant = models.CharField(max_length=25)
	rice = models.CharField(max_length=25)
	sugarcane = models.CharField(max_length=25)
	timber = models.CharField(max_length=25)
	fruit_tree = models.CharField(max_length=25)
	banana = models.CharField(max_length=25)
	coffee = models.CharField(max_length=25)
	coconut = models.CharField(max_length=25)
	citrus = models.CharField(max_length=25)
	cacao = models.CharField(max_length=25)
	mapunit = models.CharField(max_length=25)
	hectares = models.FloatField()
	acres = models.FloatField()
	perimeter = models.FloatField()
	area_kilom = models.FloatField()
	comments = models.CharField(max_length=150)
	secerosion = models.IntegerField()
	terslope = models.IntegerField()
	secslope = models.IntegerField()
	secsoil = models.CharField(max_length=30)
	capability = models.IntegerField()
	other_fea = models.CharField(max_length=25)
	water = models.CharField(max_length=25)
	erosion = models.IntegerField()
	domslope = models.IntegerField()
	domsoil = models.ForeignKey(soilFeatures, to_field='domsoil', null=True)
	soil2001_i = models.IntegerField()
	soil2001 = models.IntegerField()
	gavprimary = models.IntegerField()
	geomData = models.MultiPolygonField()
	objects = models.GeoManager()

#Rivers Model
class Rivers(models.Model):
	rivnm = models.CharField(max_length=30,default = None)
	river25_Id = models.IntegerField()
	river25 = models.IntegerField()
	length = models.FloatField()
	rpoly = models.IntegerField()
	lpoly = models.IntegerField()
	tnode = models.IntegerField()
	fnode = models.IntegerField()
	geomData = models.MultiLineStringField()
	objects = models.GeoManager()

class soilsAndRainfall(models.Model):
	soilID = models.CharField(max_length=150,default=None, null=True)
	soilCode = models.CharField(max_length=25, null=True)
	soilName = models.CharField(max_length=150, null=True)
	soilLabel = models.CharField(max_length=150, null=True)
	mapunit = models.CharField(max_length=25, null=True)
	hectares = models.FloatField()
	acres = models.FloatField()
	secerosion = models.IntegerField()
	terslope = models.IntegerField()
	secslope = models.IntegerField()
	secsoil = models.CharField(max_length=30,default=None)
	capability = models.IntegerField()
	water = models.CharField(max_length=25,default=None)
	erosion = models.IntegerField()
	domslope = models.IntegerField()
	domsoil = models.ForeignKey(soilFeatures, to_field='domsoil', null=True)
	soil2001_i = models.IntegerField()
	soil2001 = models.IntegerField()
	gavprimary = models.IntegerField()
	gridcode = models.IntegerField()
	geomData = models.GeometryField()
	objects = models.GeoManager()

#Contours Model
class Contours(models.Model):
	trt = models.IntegerField()
	trt_i = models.IntegerField()
	height = models.IntegerField()
	htm = models.FloatField()
	length = models.FloatField()
	rpoly = models.IntegerField()
	lpoly = models.IntegerField()
	tnode = models.IntegerField()
	fnode = models.IntegerField()
	geomData = models.MultiLineStringField()
	objects = models.GeoManager()

class Rainfall(models.Model):
	ranges = models.IntegerField()
	rain_range = models.CharField(max_length=30)
	class_r = models.IntegerField()
	geomData = models.PolygonField()
	objects = models.GeoManager()

class RainfallData(models.Model):
	gridcode = models.IntegerField()
	geomData = models.PolygonField()
	objects = models.GeoManager()

#Pipelines Model
class Pipelines(models.Model):
	objectID = models.IntegerField()
	pipelineID = models.IntegerField()
	size = models.IntegerField()
	datasource = models.IntegerField()
	useID = models.IntegerField()
	pipe_type = models.IntegerField()
	status = models.IntegerField()
	predecess = models.IntegerField()
	level = models.IntegerField()
	shape_length = models.FloatField()
	ownerID = models.IntegerField()
	geomData = models.GeometryField()
	objects = models.GeoManager()