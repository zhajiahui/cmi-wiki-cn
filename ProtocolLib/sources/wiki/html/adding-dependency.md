To start, you're going to want to add ProtocolLib as a dependency to your project. While you could download the jar file and add it as a classpath dependency, we highly recommend using a build system such as [Maven](https://maven.apache.org/guides/getting-started/) or [Gradle](https://docs.gradle.org/current/userguide/getting_started.html).

Maven and Gradle _should_ download the JavaDocs. If not, you can find them here: https://ci.dmulloy2.net/job/ProtocolLib/javadoc/overview-summary.html

**Maven**
```xml
<repositories>
  <repository>
    <id>dmulloy2-repo</id>
    <url>https://repo.dmulloy2.net/repository/public/</url>
  </repository>
</repositories>

<dependencies>
  <dependency>
    <groupId>com.comphenix.protocol</groupId>
    <artifactId>ProtocolLib</artifactId>
    <version>4.7.0</version>
  </dependency>
</dependencies>
```

**Gradle**
```groovy
repositories {
    maven { url "https://repo.dmulloy2.net/repository/public/" }
}

dependencies {
    compileOnly group: "com.comphenix.protocol", name: "ProtocolLib", version: "4.7.0";
}
```

### [Next Page](https://github.com/dmulloy2/ProtocolLib/wiki/ProtocolManager)