# Lumeer Sample Data

This repository contains data set which can be imported to Lumeer.

## Prerequisites

Install lumeer-utils from Lumeer/engine project into your local repository:
```
engine/ $ mvn install
```

## Import

In order to import the data to Lumeer, you can run `import.sh` or `import.bat`.
If you need to change URL of a running engine, edit `pom.xml`.

See [https://github.com/Lumeer/engine/tree/devel/utils/src/test/resources] for sample data files.

If you run into permission issues, you can tepmorarily change `checkRole()` body in `SecurityFacade` to ignore permissions.
```
return true;
```