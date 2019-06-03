<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:atom="http://www.w3.org/2005/Atom">

	<xsl:template match="/">
		<html>
			<head>
				<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
				<meta name="theme-color" content="#222"/>
				<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent"/>
				<title><xsl:value-of select="/atom:feed/atom:title"/></title>
				<style>
					img {
						display: block;
						margin: 1% auto;
					}
				</style>
			</head>
			<body>
				<xsl:apply-templates select="/atom:feed"/>
			</body>
		</html>
	</xsl:template>

	<xsl:template match="/atom:feed">
		<xsl:apply-templates select="atom:entry"/>
	</xsl:template>

	<xsl:template match="atom:entry">
		<xsl:for-each select=".">
			<xsl:value-of select="atom:content" disable-output-escaping="yes"/>
		</xsl:for-each>
	</xsl:template>

</xsl:stylesheet>