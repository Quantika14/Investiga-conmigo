#!/usr/bin/env python
#-*- coding:utf-8 -*-

#AUTHOR: JORGE WEBSEC
import csv, urllib2, json, time

count = 0
count_win = 0
archs = ["Concejales/Sevilla.csv", "Concejales/Almeria.csv", "Concejales/Cadiz.csv", "Concejales/Huelva.csv", "Concejales/Malaga.csv", "Concejales/Granada.csv","Concejales/Cordoba.csv", "Concejales/Jaen.csv"]

def saveData(name, a, d, f, p, l):
	print "************************"
	with open("resultados.csv", "a") as f:
		data = str(name) + "," + str(a) + "," + str(d) + "," + str(f) + "," + str(p) + "," + str(l) + "\n"
		f.write(data)
	f.close()
	print "[GUARDADO]"

def libreborme(target, fecha, partido, lugar):
	global count, count_win
	url = "https://libreborme.net/borme/api/v1/persona/search/?q=" + target + "&page=1"
	html = urllib2.urlopen(url).read()
	j = json.loads(html)

	name = target.replace("+", " ")
	print "TARGET-> " + name
	
	if not """{"objects": []}""" in html:
		target = j["objects"][0]["resource_uri"]
		web = "https://libreborme.net/" + target
		html = urllib2.urlopen(web).read()
		datas = json.loads(html)
		print "-----------Empresas:"
		if datas["cargos_historial"]:
			print "[+]Cargos en empresas anteriores:"
			print datas["cargos_historial"]
		else:
			pass

		if datas["cargos_actuales"]:
			count_win += 1
			print "[+]Cargos en empresas actualmente:"
			print datas["cargos_actuales"]
		else:
			pass
		print ""
			

		count += 1
		saveData(name, datas["cargos_historial"], datas["cargos_actuales"], fecha, partido, lugar)
	else:
		print "[INFO] No aparece en el BORME..."


	time.sleep(5)


def main():
	#Buscamos uno a uno en cada provincia
	for concejal in archs:
		#Abrimos el archivo
		with open(concejal as csvarchivo:
			entrada = csv.reader(csvarchivo)
			for reg in entrada:
				target = reg[1] + " " + reg[2] + " " + reg[3]
				#Buscamos en Libreborme
				libreborme(target.replace(" ", "+"), reg[4], reg[5], reg[0])
			csvarchivo.close()
main()
