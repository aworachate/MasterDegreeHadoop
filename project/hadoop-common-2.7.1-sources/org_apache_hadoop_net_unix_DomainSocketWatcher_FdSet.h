/* DO NOT EDIT THIS FILE - it is machine generated */
#include <jni.h>
/* Header for class org_apache_hadoop_net_unix_DomainSocketWatcher_FdSet */

#ifndef _Included_org_apache_hadoop_net_unix_DomainSocketWatcher_FdSet
#define _Included_org_apache_hadoop_net_unix_DomainSocketWatcher_FdSet
#ifdef __cplusplus
extern "C" {
#endif
/*
 * Class:     org_apache_hadoop_net_unix_DomainSocketWatcher_FdSet
 * Method:    alloc0
 * Signature: ()J
 */
JNIEXPORT jlong JNICALL Java_org_apache_hadoop_net_unix_DomainSocketWatcher_00024FdSet_alloc0
  (JNIEnv *, jclass);

/*
 * Class:     org_apache_hadoop_net_unix_DomainSocketWatcher_FdSet
 * Method:    add
 * Signature: (I)V
 */
JNIEXPORT void JNICALL Java_org_apache_hadoop_net_unix_DomainSocketWatcher_00024FdSet_add
  (JNIEnv *, jobject, jint);

/*
 * Class:     org_apache_hadoop_net_unix_DomainSocketWatcher_FdSet
 * Method:    remove
 * Signature: (I)V
 */
JNIEXPORT void JNICALL Java_org_apache_hadoop_net_unix_DomainSocketWatcher_00024FdSet_remove
  (JNIEnv *, jobject, jint);

/*
 * Class:     org_apache_hadoop_net_unix_DomainSocketWatcher_FdSet
 * Method:    getAndClearReadableFds
 * Signature: ()[I
 */
JNIEXPORT jintArray JNICALL Java_org_apache_hadoop_net_unix_DomainSocketWatcher_00024FdSet_getAndClearReadableFds
  (JNIEnv *, jobject);

/*
 * Class:     org_apache_hadoop_net_unix_DomainSocketWatcher_FdSet
 * Method:    close
 * Signature: ()V
 */
JNIEXPORT void JNICALL Java_org_apache_hadoop_net_unix_DomainSocketWatcher_00024FdSet_close
  (JNIEnv *, jobject);

#ifdef __cplusplus
}
#endif
#endif
